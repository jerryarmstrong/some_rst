src/index.tsx
=============

Last edited: 2022-06-29 05:55:18

Contents:

.. code-block:: tsx

    import React from "react";
import ReactDOM from "react-dom";

import {
  WalletProvider,
  ConnectionProvider,
  ColorModeContextProvider,
} from "./contexts";

import "antd/dist/antd.css";
import "@fontsource/open-sans";
import "@fontsource/roboto";
import "@fontsource/sora";

import App from "./App";
import reportWebVitals from "./reportWebVitals";

// import "./index.css";

ReactDOM.render(
  <React.StrictMode>
    <ConnectionProvider>
      <WalletProvider>
        <ColorModeContextProvider>
          <App />
        </ColorModeContextProvider>
      </WalletProvider>
    </ConnectionProvider>
  </React.StrictMode>,
  document.getElementById("root")
);

reportWebVitals();


