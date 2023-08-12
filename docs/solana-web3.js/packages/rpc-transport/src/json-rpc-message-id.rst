packages/rpc-transport/src/json-rpc-message-id.ts
=================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    let _nextMessageId = 0;
export function getNextMessageId() {
    const id = _nextMessageId;
    _nextMessageId = (_nextMessageId + 1) % Number.MAX_SAFE_INTEGER;
    return id;
}


