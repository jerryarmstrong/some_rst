packages/eslint-config-custom/shared/extensions.js
==================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    const jsExtensions = [".js", ".jsx"];
const tsExtensions = [".ts", ".tsx", ".d.ts"];

const platformSubextensions = [".android", ".ios", ".web", ".native"];

function computeExpoExtensions(baseExtensions, platformSubextensions) {
  const expoExtensions = [];
  for (const expo of [".expo", ""]) {
    for (const platform of [...platformSubextensions, ""]) {
      for (const base of baseExtensions) {
        expoExtensions.push(`${expo}${platform}${base}`);
      }
    }
  }
  return expoExtensions;
}

module.exports = {
  jsExtensions,
  tsExtensions,
  platformSubextensions,
  computeExpoExtensions,
};


