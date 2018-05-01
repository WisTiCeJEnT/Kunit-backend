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