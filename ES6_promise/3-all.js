/* eslint-disable */
import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photoResponse, userResponse]) => {
      console.log(`firstName: ${userResponse.firstName}, lastName: ${userResponse.lastName}, body: ${photoResponse.body}`);
    })
    .catch(error => {
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;

