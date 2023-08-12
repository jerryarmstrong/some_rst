src/v2/components/UI/TableNav/styles.js
=======================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  root: {
    display: 'flex',
    justifyContent: 'flex-end',
    marginTop: 10,
    '& a': {
      display: 'flex',
      color: getColor('white')(theme),
    },
  },
}));


