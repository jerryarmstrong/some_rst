src/v2/components/Blocks/Table/styles.js
========================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';

export default makeStyles(theme => ({
  root: {
    [theme.breakpoints.down('sm')]: {
      padding: 0,
      paddingBottom: 27,
      marginBottom: 50,
    },
  },
  list: {
    width: '100%',
  },
  vertical: {
    [theme.breakpoints.down('sm')]: {
      flexDirection: 'column',
    },
  },
}));


