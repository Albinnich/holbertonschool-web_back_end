// 3-correct-text.test.js

import handleProfileSignup from './3-all';

test('handleProfileSignup returns the right text', async () => {
  // Mock console.log to spy on its calls
  const spy = jest.spyOn(console, 'log').mockImplementation();

  // Execute the function
  await handleProfileSignup();

  // Assert that console.log was called with the correct format
  expect(spy).toBeCalledWith('photo-profile-1 Guillaume Salva');

  // Restore the original implementation of console.log
  spy.mockRestore();
});

