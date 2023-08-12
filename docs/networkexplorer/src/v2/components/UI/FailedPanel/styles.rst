src/v2/components/UI/FailedPanel/styles.js
==========================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  root: {
    paddingTop: 50,
    marginBottom: 'auto',
  },
  body: {
    backgroundColor: getColor('grey')(theme),
    padding: 15,
    textTransform: 'uppercase',
    display: 'flex',
    alignItems: 'center',
    color: getColor('pink')(theme),
    '& svg': {
      marginRight: 15,
    },
  },
  text: {
    fontWeight: 'bold',
    '& a': {
      color: getColor('main')(theme),
    },
  },
}));


