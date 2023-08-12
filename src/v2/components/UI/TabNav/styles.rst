src/v2/components/UI/TabNav/styles.js
=====================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  tab: {
    border: `1px solid ${getColor('main')(theme)}`,
    color: getColor('main')(theme),
    opacity: 1,
  },
  tabSelected: {
    backgroundColor: getColor('main')(theme),
    color: getColor('dark')(theme),
  },
}));


