# drop table ClubMember;
# drop table WMSTSections;
# drop table PersonalInfo;
# drop table HonorRollInfo;
# drop table StudentInfo;

create table WMSTSections(
    ClassSection int primary key auto_increment,
    Professor varchar(50)
);

create table StudentInfo(
    #DepartmentId int
    MajorId int primary key auto_increment,
    Major varchar(25)
);

create table PersonalInfo(
    CountyId int primary key auto_increment,
    County varchar(20)
);

create table HonorRollInfo(
    HonorRollId int primary key auto_increment,
    GPA decimal(2,1),
    HonorRoll int
);

create table ClubMember (
    StudentId int primary key auto_increment,
    FirstName varchar(50) NOT NULL,
    LastName varchar(50) NOT NULL,
    ClassSection int,
    MajorId int,
    CountyId int,
    #GPA decimal(2,1),
    HonorRollId int,
    FOREIGN KEY (ClassSection) references WMSTSections(ClassSection),
    FOREIGN KEY (MajorId) references StudentInfo(MajorId),
    FOREIGN KEY (CountyId) references PersonalInfo(CountyId),
    FOREIGN KEY (HonorRollId) references HonorRollInfo(HonorRollId)
);