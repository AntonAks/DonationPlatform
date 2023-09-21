// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

// Contract - 0xB0628ee92134b58Cd88eF36020c0DDA49bD97eb9

contract DonatePlatform {

    address public owner;

    struct Project {
        uint projectId;
        string projectTitle;
        address projectOwner;
        uint256 projectGoal;
        uint256 dateExpiration;
        uint totalDonations;
        bool isClosed;
        address[] donors;
    }

    struct Donation {
        uint projectId;
        address donor;
        uint256 amount;
    }

    Donation[] public donations;

    mapping(uint => Project) public projects;
    uint[] internal projectIds;

    uint public totalProjects;
    uint public totalDonations;

    mapping(address => Donation[]) internal donationsByDonor;

    event ProjectCreated(uint projectId, string projectTitle, address projectOwner, uint256 projectGoal, uint256 dateExpiration);
    event ProjectClosed(uint projectId, string projectTitle, address projectOwner, uint256 projectGoal, uint256 dateExpiration, uint totalDonations, bool isClosed);
    event DonationMade(uint projectId, address donor, uint256 amount);


    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    function isProjectExistsByName(string memory _projectTitle) internal view returns(bool) {
        for (uint i = 0; i < projectIds.length; i++) {
            Project storage project = projects[projectIds[i]];
            if (keccak256(abi.encodePacked(project.projectTitle)) == keccak256(abi.encodePacked(_projectTitle))) {
                return true;
            }
        }
        return false;
    }

    function createProject(string memory _projectTitle, address _projectOwner, uint256 _projectGoal, uint256 _dateExpiration) onlyOwner public returns(uint) {
        require(_projectGoal > 0, "Project goal must be greater than 0.");
        require(_dateExpiration > block.timestamp, "Expiration date must be greater than current date.");
        require(isProjectExistsByName(_projectTitle) == false, "Project already exists.");
        totalProjects++;
        uint projectId = totalProjects;
        projects[projectId] = Project(projectId, _projectTitle, _projectOwner, _projectGoal, _dateExpiration, 0, false, new address[](0));
        projectIds.push(projectId);
        emit ProjectCreated(projectId, _projectTitle, _projectOwner, _projectGoal, _dateExpiration);
        return projectId;
    }

    function closeProject(uint _projectId) onlyOwner public {
        Project storage project = projects[_projectId];
        require(project.projectId != 0, "Project does not exist.");
        require(project.isClosed == false, "Project is already closed.");
        project.isClosed = true;
        emit ProjectClosed(project.projectId, project.projectTitle, project.projectOwner, project.projectGoal, project.dateExpiration, project.totalDonations, project.isClosed);
    }

    function donate(uint _projectId) public payable {
        Project storage project = projects[_projectId];
        require(project.projectId != 0, "Project does not exist.");
        require(project.isClosed == false, "Project is closed.");
        require(project.dateExpiration > block.timestamp, "Project is expired.");
        require(msg.value > 0, "Donation amount must be greater than 0.");
        project.totalDonations += msg.value;
        totalDonations += msg.value;
        project.donors.push(msg.sender);
        donations.push(Donation(_projectId, msg.sender, msg.value));
        donationsByDonor[msg.sender].push(Donation(_projectId, msg.sender, msg.value));
        emit DonationMade(_projectId, msg.sender, msg.value);
    }

    function getProjectIds() public view returns(uint[] memory) {
        return projectIds;
    }

    function getProject(uint _projectId) public view returns(uint projectId, string memory projectTitle, address projectOwner, uint256 projectGoal, uint256 dateExpiration, uint totalDonations, bool isClosed) {
        Project storage project = projects[_projectId];
        return (project.projectId, project.projectTitle, project.projectOwner, project.projectGoal, project.dateExpiration, project.totalDonations, project.isClosed);
    }

    function getDonationsByDonor(address _donor) public view returns(Donation[] memory) {
        return donationsByDonor[_donor];
    }

    function cancelProject(uint _projectId) public onlyOwner {
        Project storage project = projects[_projectId];
        require(project.projectId != 0, "Project does not exist.");
        require(project.isClosed == false, "Project is already closed.");
        project.isClosed = true;
        emit ProjectClosed(project.projectId, project.projectTitle, project.projectOwner, project.projectGoal, project.dateExpiration, project.totalDonations, project.isClosed);
    }

    function withdrawToProjectOwner(uint _projectId) onlyOwner public {
        Project storage project = projects[_projectId];
        require(project.projectId != 0, "Project does not exist.");
        require(project.isClosed == true, "Project is not closed.");
        payable(project.projectOwner).transfer(project.totalDonations);
    }
}

