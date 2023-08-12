src/v2/components/UI/CTypography/styles.js
==========================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';

import getColor from '../../../utils/getColor';

export default makeStyles(theme => ({
  root: {},
  caption: {
    letterSpacing: 2.5,
    color: getColor('caption')(theme),
    fontSize: 15,
  },
  text: {},
}));


