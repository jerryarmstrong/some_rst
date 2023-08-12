packages/chat-sdk/src/components/messageInput/getActiveToken.ts
===============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export function getActiveToken(
  input: string,
  cursorPosition: number | undefined
) {
  const tokenizedQuery = input.split(/[\s\n]/).reduce((acc, word, index) => {
    const previous = acc[index - 1];
    const start = index === 0 ? index : previous.range[1] + 1;
    const end = start + word.length;

    return acc.concat([{ word, range: [start, end] }]);
  }, [] as Array<{ word: string; range: [number, number] }>);

  if (cursorPosition === undefined) {
    return undefined;
  }

  const activeToken = tokenizedQuery.find(
    ({ range }) => range[0] < cursorPosition && range[1] >= cursorPosition
  );

  return activeToken;
}


