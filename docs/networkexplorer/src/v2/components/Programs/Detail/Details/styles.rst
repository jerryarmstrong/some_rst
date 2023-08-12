src/v2/components/Programs/Detail/Details/styles.js
===================================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  list: {
    padding: 0,
    margin: 0,
  },
  item: {
    display: 'flex',
    alignItems: 'center',
    marginBottom: 40,
    '& > div:first-child': {
      width: 176,
      [theme.breakpoints.down('sm')]: {
        marginBottom: 5,
      },
    },
    '& > div:last-child': {
      display: 'flex',
      alignItems: 'center',
      '& > span': {
        marginLeft: 15,
        color: getColor('main')(theme),
      },
    },
    [theme.breakpoints.down('sm')]: {
      flexDirection: 'column',
      alignItems: 'flex-start',
    },
  },
}));


