app/popup/index.tsx
===================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React from "react"
import ReactDOM from "react-dom"
import "./index.css"
import { App } from "./pages/app"
import { unregisterServiceWorker } from "./core/service-worker"

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
)

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
unregisterServiceWorker()


