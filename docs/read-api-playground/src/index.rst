src/index.tsx
=============

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: tsx

    import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import { ReusableProvider } from "reusable";

ReactDOM.render(
  <ReusableProvider>
    <App />
  </ReusableProvider>
, document.getElementById("root"));


