src/v2/components/TourDeSol/styles.js
=====================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => ({
  stages: {
    display: 'flex',
    width: '100%',
    padding: 0,
    margin: 0,
    marginLeft: 'auto',
    maxWidth: 675,
    [theme.breakpoints.down('sm')]: {
      maxWidth: '100%',
      marginLeft: 0,
    },
  },
  stage: {
    height: 55,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    color: getColor('white')(theme),
    padding: '0 15px',
    fontSize: 15,
    lineHeight: 1,
    textTransform: 'uppercase',
    lettersSpacing: 2.5,
    border: `1px solid ${getColor('grey3')(theme)}`,
    flex: 1,
    fontWeight: 'bold',
    '&:not(:first-child)': {
      borderLeft: 'none',
    },
    '& span': {
      fontSize: 10,
      marginTop: 3,
      fontWeight: 'normal',
    },
  },
  stageActive: {
    background: getColor('main')(theme),
    color: getColor('dark')(theme),
    borderColor: getColor('main')(theme),
  },
  leftCol: {
    display: 'flex',
    flexDirection: 'column',
  },
}));


