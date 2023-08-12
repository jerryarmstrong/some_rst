src/v2/components/QRPopup/styles.js
===================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  qrBtn: {
    color: getColor('main')(theme),
    border: `1px solid ${getColor('main')(theme)}`,
    fontSize: 10,
    textTransform: 'uppercase',
    height: 18,
    width: 55,
    background: 'transparent',
    padding: 0,
  },
  popup: {
    padding: 10,
    background: getColor('white')(theme),
  },
}));


