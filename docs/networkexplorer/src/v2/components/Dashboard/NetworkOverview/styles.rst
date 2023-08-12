src/v2/components/Dashboard/NetworkOverview/styles.js
=====================================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  row: {
    marginBottom: 8,
  },
  betaLabel: {
    fontSize: 15,
    color: getColor('main')(theme),
    lineHeight: 1,
  },
  card: {
    height: 306,
  },
  mapCard: {
    height: 306,
    '& > svg': {
      width: '100%',
      height: 295,
      minHeight: 290,
      marginTop: -5,
    },
  },
  tpsCard: {
    '& > svg': {
      width: '100%',
      marginTop: -5,
      height: 295,
      minHeight: 290,
    },
  },
}));


