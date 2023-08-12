src/v2/components/Dashboard/NetworkOverview/StatCards/styles.js
===============================================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  card: {
    height: 164,
    '& svg': {
      width: '100%',
      height: 150,
      marginTop: -2,
    },
  },
  val: {
    fontSize: 60,
    fontWeight: 'bold',
    color: getColor('main')(theme),
    margin: '20px 0',
  },
  leader: {
    textDecoration: 'none',
    '& h2': {
      fontSize: 30,
      lineHeight: 1.3,
      fontWeight: 'bold',
      color: getColor('main')(theme),
      marginTop: 25,
      letterSpacing: 3.4,
    },
  },
  changes: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  tooltip: {
    backgroundColor: getColor('white')(theme),
    color: getColor('dark')(theme),
    fontSize: 12,
    lineHeight: '16px',
    borderRadius: 0,
    padding: 11,
    whiteSpace: 'nowrap',
    maxWidth: '100%',
  },
}));


