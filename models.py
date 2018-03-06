class Student(object):
    def __init__(self, nuid, firstname, middlename, lastname, gender, email, photo, campus, enrollmentstatus, startterm, expectedgraduation, privacy):
        self.nuid = nuid
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.photo = photo
        self.campus = campus
        self.enrollmentstatus = enrollmentstatus
        self.startterm = startterm
        self.expectedgraduation = expectedgraduation
        self.privacy = privacy

    def __repr__(self):
        return "Student({:d}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})"\
            .format(self.nuid, self.firstname, self.middlename, self.lastname, self.gender, self.email, self.photo, self.campus, self.enrollmentstatus, self.startterm, self.expectedgraduation, self.privacy)

    def serialize(self):
        return {
            "nuid" : self.nuid,
            "firstname" : self.firstname,
            "middlename" : self.middlename,
            "lastname" : self.lastname,
            "gender" : self.gender,
            "email" : self.email,
            "photo" : self.photo,
            "campus" : self.campus,
            "enrollmentstatus" : self.enrollmentstatus,
            "startterm" : self.startterm,
            "expectedgraduation" : self.expectedgraduation,
            "privacy" : self.privacy
        }


class Experience(object):
    def __init__(self, id, companyname, title, startdate, enddate, description):
        self.id = id
        self.companyname = companyname
        self.title = title
        self.startdate = startdate
        self.enddate = enddate
        self.description = description

    def __repr__(self):
        return "WorkExperience({:d}, {}, {}, {}, {}, {})"\
            .format(self.id, self.companyname, self.title, self.startdate, self.enddate, self.description)

    def serialize(self):
        return {
            "id" : self.id,
            "companyname" : self.companyname,
            "title" : self.title,
            "startdate" : self.startdate,
            "enddate" : self.enddate,
            "description" : self.description
        }