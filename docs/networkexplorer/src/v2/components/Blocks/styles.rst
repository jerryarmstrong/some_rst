src/v2/components/Blocks/styles.js
==================================

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
    justifyContent: 'flex-end',
    marginTop: 10,
    '& a': {
      display: 'flex',
      color: getColor('white')(theme),
    },
  },
}));


