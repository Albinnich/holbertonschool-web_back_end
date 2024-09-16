// Display welcome message
console.log('Welcome to Holberton School, what is your name?');

// Read input from the user
process.stdin.on('data', (input) => {
  const name = input.toString().trim(); // Trim to remove trailing newline characters
  console.log(`Your name is: ${name}`);

  // End the input stream and display the closing message
  process.stdin.end(); // Properly end the input stream
});

// Listen for the 'end' event to display the closing message
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
