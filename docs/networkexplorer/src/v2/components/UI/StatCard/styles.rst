src/v2/components/UI/StatCard/styles.js
=======================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  root: {
    background: getColor('grey')(theme),
    color: '#fff',
    borderRadius: 0,
    height: '100%',
    padding: '17px 15px',
  },
  header: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    '& span': {
      whiteSpace: 'nowrap',
      overflow: 'hidden',
      textOverflow: 'ellipsis',
    },
  },
  value: {
    fontSize: 40,
    fontWeight: 'bold',
    color: getColor('main')(theme),
    margin: '20px 0',
  },
  changes: {
    display: 'flex',
    justifyContent: 'center',
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
  },
}));


