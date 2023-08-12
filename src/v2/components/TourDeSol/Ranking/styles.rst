src/v2/components/TourDeSol/Ranking/styles.js
=============================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  root: {
    background: getColor('grey2')(theme),
    padding: '17px 24px',
  },
  list: {
    padding: 0,
  },
  item: {
    display: 'flex',
    alignItems: 'center',
    '&:not(:last-child)': {
      marginBottom: 17,
    },
  },
  name: {
    width: 130,
    marginRight: 26,
    flexShrink: 0,
  },
  bar: {
    flex: 1,
    height: 8,
    borderRadius: 10,
    background: getColor('greyW1')(theme),
    position: 'relative',
  },
  icon: {
    position: 'absolute',
    top: '50%',
    transform: 'translateY(-50%)',
    transition: 'left .15s ease-in-out',
  },
}));


