config/helper.js
================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: js

    const fs = require("fs")
const path = require("path")

const appDirectory = fs.realpathSync(process.cwd())

const resolveApp = (relativePath) => {
  return path.resolve(appDirectory, relativePath)
}

module.exports = {
  resolveApp: resolveApp,
}


