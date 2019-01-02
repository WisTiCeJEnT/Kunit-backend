# KUnit Backend

## API Documentation
Replace "URL" with "https://kunit-backend.herokuapp.com" if you want to use our backend server
#### Checking status
        GET : URL/      (root)

#### Create new KUDS (KUnit Data Structure)
        GET : URL/new
Return a empty KUDS
#### Adding subject to KUDS
        GET : URL/add/{subjectID}a{oldKUDS}
Return a new categorized KUDS
#### Removing subject from KUDS
        GET : URL/remove/{subjectID}d{oldKUDS}
Return a new categorized KUDS
#### Required unit of each major
        GET : URL/unitOf/{majorID}
Return list of integer in json format. The list is ordered by Wellness,Entrepreneurship,Thai Citizen and Global Citizen,Language and Communicationand Aesthetics
