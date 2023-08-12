src/v2/components/Programs/Detail/Code/styles.js
================================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  header: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    marginBottom: 17,
    '& a': {
      marginLeft: 15,
    },
  },
  code: {
    maxHeight: 456,
    overflowY: 'auto',
    backgroundColor: getColor('grey')(theme),
    padding: 39,
    color: getColor('white')(theme),
    '& code': {
      whiteSpace: 'pre-wrap',
      letterSpacing: 2,
      fontSize: 15,
      lineHeight: '100%',
      display: 'block',
    },
  },
}));


