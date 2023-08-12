server.js
=========

Last edited: 2020-08-30 15:21:22

Contents:

.. code-block:: js

    import express from 'express';
import path from 'path';

const port = process.env.PORT || 8080;
const app = express();

app.use(express.static(path.join(__dirname, 'dist')));

app.get('*', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'dist/index.html'));
});
console.log(`Listening on port ${port}`);
app.listen(port);


