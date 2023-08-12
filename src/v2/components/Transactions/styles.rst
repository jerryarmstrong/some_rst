src/v2/components/Transactions/styles.js
========================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  total: {
    marginRight: 'auto',
    marginLeft: 15,
  },
  nav: {
    display: 'flex',
    marginTop: 10,
    '& a': {
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: getColor('white')(theme),
      color: getColor('dark')(theme),
      marginRight: 1,
    },
  },
}));


