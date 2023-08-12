apps/payment-ui/src/features/websocket/websocketSlice.ts
========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { RootState } from '@/store';
import { createSlice } from '@reduxjs/toolkit';

export enum WebsocketSesssionState {
    fresh, // on page load
    readyToConnect, // websocket is ready to try and connect again
    connected, // websocket is connected
    closed, // websocket is closed
    error, // terminal error state
}

export interface WebsocketState {
    sessionState: WebsocketSesssionState;
}

const initalState: WebsocketState = {
    sessionState: WebsocketSesssionState.fresh,
};

const websocketSlice = createSlice({
    name: 'websocket',
    initialState: initalState,
    reducers: {
        setWebsocketReadyToConnect: state => {
            state.sessionState = WebsocketSesssionState.readyToConnect;
        },
        setWebsocketConnected: state => {
            state.sessionState = WebsocketSesssionState.connected;
        },
        setWebsocketClosed: state => {
            state.sessionState = WebsocketSesssionState.closed;
        },
        setWebsocketError: state => {
            state.sessionState = WebsocketSesssionState.error;
        },
    },
});

export const { setWebsocketReadyToConnect, setWebsocketConnected, setWebsocketClosed, setWebsocketError } =
    websocketSlice.actions;

export default websocketSlice.reducer;

export const getWebsocketSessionState = (state: RootState): WebsocketSesssionState => state.websocket.sessionState;


