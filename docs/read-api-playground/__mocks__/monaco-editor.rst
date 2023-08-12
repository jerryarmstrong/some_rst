__mocks__/monaco-editor.js
==========================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: js

    class Selection {
  //
};

const monaco = {
  addAction() {

  },
  getModels() {
    return []
  },
  Uri: {
    parse(f) {
      return f;
    }
  },
  KeyCode: {},
  KeyMod: {
    chord() {

    }
  },
  get editor() {
    return this;
  },
  languages: {
    json: {
      jsonDefaults: {
        setDiagnosticsOptions() {
        }
      }
    }
  },
  setSelection() {

  },
  focus() {

  },
  Selection,
  onDidChangeModelContent() {

  },
  setModel() {

  },
  createModel() {
    return {
      updateOptions() {

      }
    }
  },
  create() {
    return this;
  },
  dispose() {},
  getModelMarkers() {
    return []
  }
};

module.exports = monaco;


