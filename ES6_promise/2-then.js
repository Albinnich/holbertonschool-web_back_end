/* eslint-disable */
/*function handleResponseFromAPI(promise) {
  promise.then(
    (response) => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success'
      };
     },
     (error) => {
       console.log('Got a response from the API');
       return new Error();
      }
  );
}

export default handleResponseFromAPI;*/

function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success'
      };
    })
    .catch(() => {
      console.log('Got a response from the API');
      return new Error();
    });
}

export default handleResponseFromAPI;
