api/views/accounts/index.js
===========================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import _ from 'lodash';

/**
 * AccountIndexView : supports the account index page
 *
 * Changes:
 *   - 20190912.01 : initial version
 */
const __VERSION__ = 'AccountIndexView@1.0.0';
export class AccountIndexView {
  asVersion(rawData, __errors__, version) {
    if (__errors__) {
      return {
        __VERSION__,
        __errors__,
      };
    }

    const timelineData = rawData.timelinePage;
    const timelineInfo = rawData.timelineInfo;

    const results = _.map(timelineData.results, result => {
      const [k, x] = result;
      const program_id = x.program_id;
      const timestamp = x.timestamp;

      return [
        k,
        {
          program_id,
          timestamp,
        },
      ];
    });

    const pageData = {
      timeline: timelineData.timeline,
      start: timelineData.start,
      results,
      length: timelineData.length,
      count: timelineData.count,
      next: timelineData.next,
      prev: timelineData.prev,
      timestamp: timelineData.dt,
    };

    const pageInfo = {
      timeline: timelineInfo.timeline,
      last: timelineInfo.last,
      first: timelineInfo.first,
      count: timelineInfo.count,
      timestamp: timelineInfo.dt,
    };

    if (version === 'AccountIndexView@latest' || version === __VERSION__) {
      return {
        __VERSION__,
        pageData,
        pageInfo,
      };
    }

    return {
      error: 'UnsupportedVersion',
      currentVersion: __VERSION__,
      desiredVersion: version,
    };
  }
}


