src/v2/components/Search/styles.js
==================================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import {makeStyles} from '@material-ui/core/styles';
import getColor from 'v2/utils/getColor';

export default makeStyles(theme => {
  return {
    root: {
      position: 'relative',
    },
    form: {
      border: `1px solid ${getColor('grey')(theme)}`,
      padding: 5,
      display: 'flex',
    },
    inputInput: {
      overflow: 'hidden',
      textOverflow: 'ellipsis',
      whiteSpace: 'nowrap',
    },
    input: {
      border: 'none',
      background: getColor('grey2')(theme),
      height: 40,
      width: '100%',
      padding: '0 20px',
    },
    btn: {
      background: getColor('main')(theme),
      borderRadius: 0,
      width: 40,
    },
    list: {
      position: 'absolute',
      background: getColor('white')(theme),
      width: '100%',
      padding: '12px 20px',
      '& ul': {
        padding: 0,
        margin: 0,
        '& a': {
          color: getColor('grey3')(theme),
          fontSize: 12,
          textDecoration: 'none',
          padding: '5px 0',
          display: 'block',
          whiteSpace: 'nowrap',
          overflow: 'hidden',
          textOverflow: 'ellipsis',
          '&:hover': {
            color: getColor('dark')(theme),
          },
        },
      },
    },
    title: {
      color: getColor('dark')(theme),
    },
  };
});


