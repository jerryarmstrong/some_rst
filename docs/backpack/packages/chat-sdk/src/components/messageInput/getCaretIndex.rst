packages/chat-sdk/src/components/messageInput/getCaretIndex.ts
==============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export function getCaretIndex(element) {
  if (!element) {
    return 0;
  }
  let position: number | undefined = 0;
  const isSupported = typeof window.getSelection !== "undefined";
  if (isSupported) {
    const selection = window.getSelection();
    if (selection?.rangeCount !== 0) {
      const range = window?.getSelection()?.getRangeAt(0);
      const preCaretRange = range?.cloneRange();
      if (range) {
        preCaretRange?.selectNodeContents(element);
        preCaretRange?.setEnd(range?.endContainer, range?.endOffset);
        position = preCaretRange?.toString().length;
      }
    }
  }
  return position;
}


