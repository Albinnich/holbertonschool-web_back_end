/* eslint-disable */
function signUpUser(firstName, lastName) {
signUpUser('John', 'Doe')
  .then(user => {
    console.log('User signed up:', user);
  })
  .catch(error => {
    console.error('Error signing up:', error);
  });

