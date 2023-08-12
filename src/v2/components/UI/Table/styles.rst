src/v2/components/UI/Table/styles.js
====================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';

export default makeStyles(() => ({
  root: {
    maxWidth: '100%',
    '& .MuiTableCell-root.MuiTableCell-body': {
      maxWidth: 1,
      overflow: 'hidden',
      textOverflow: 'ellipsis',
      '& > *': {
        overflow: 'hidden',
        textOverflow: 'ellipsis',
        display: 'block',
      },
    },
  },
}));


