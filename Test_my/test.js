// Copyright 2012 Google Inc. All rights reserved.

(function() {

  var data = {
      "resource": {
          "version": "13",

          "macros": [{
              "function": "__e"
          }, {
              "function": "__e"
          }, {
              "function": "__v",
              "vtp_dataLayerVersion": 1,
              "vtp_setDefaultValue": false,
              "vtp_name": "eventCategory"
          }, {
              "function": "__v",
              "vtp_dataLayerVersion": 1,
              "vtp_setDefaultValue": false,
              "vtp_name": "eventAction"
          }, {
              "function": "__v",
              "vtp_dataLayerVersion": 1,
              "vtp_setDefaultValue": false,
              "vtp_name": "eventLabel"
          }, {
              "function": "__u",
              "vtp_component": "URL",
              "vtp_enableMultiQueryKeys": false,
              "vtp_enableIgnoreEmptyQueryParam": false
          }, {
              "function": "__k",
              "vtp_decodeCookie": false,
              "vtp_name": "wp_mkg_uid"
          }, {
              "function": "__smm",
              "vtp_setDefaultValue": false,
              "vtp_input": ["macro", 0],
              "vtp_map": ["list", ["map", "key", "TopDevGames", "value", "top_dev_games"], ["map", "key", "UnderGame", "value", "under_game"], ["map", "key", "LatestGames", "value", "latest_games"]]
          }, {
              "function": "__smm",
              "vtp_setDefaultValue": false,
              "vtp_input": ["macro", 3],
              "vtp_map": ["list", ["map", "key", "Search", "value", "search"]]
          }, {
              "function": "__smm",
              "vtp_setDefaultValue": false,
              "vtp_input": ["macro", 3],
              "vtp_map": ["list", ["map", "key", "FullScreen", "value", "full_screen"], ["map", "key", "IssueReport", "value", "issue_report"], ["map", "key", "VideoReview", "value", "video_review"], ["map", "key", "Bookmark", "value", "bookmark"]]
          }, {
              "function": "__f",
              "vtp_component": "URL"
          }, {
              "function": "__u",
              "vtp_stripWww": false,
              "vtp_component": "HOST",
              "vtp_enableMultiQueryKeys": false,
              "vtp_enableIgnoreEmptyQueryParam": false
          }, {
              "function": "__u",
              "vtp_component": "PATH",
              "vtp_defaultPages": ["list"],
              "vtp_enableMultiQueryKeys": false,
              "vtp_enableIgnoreEmptyQueryParam": false
          }, {
              "function": "__u",
              "vtp_component": "URL",
              "vtp_enableMultiQueryKeys": false,
              "vtp_enableIgnoreEmptyQueryParam": false
          }, {
              "function": "__smm",
              "vtp_setDefaultValue": false,
              "vtp_input": ["macro", 0],
              "vtp_map": ["list", ["map", "key", "ReadMore", "value", "read_more"], ["map", "key", "TableOfContent", "value", "table_of_content"]]
          }, {
              "function": "__u",
              "vtp_component": "URL",
              "vtp_enableMultiQueryKeys": false,
              "vtp_enableIgnoreEmptyQueryParam": false
          }, {
              "function": "__u",
              "vtp_component": "HOST",
              "vtp_enableMultiQueryKeys": false,
              "vtp_enableIgnoreEmptyQueryParam": false
          }, {
              "function": "__u",
              "vtp_component": "PATH",
              "vtp_enableMultiQueryKeys": false,
              "vtp_enableIgnoreEmptyQueryParam": false
          }, {
              "function": "__f",
              "vtp_component": "URL"
          }, {
              "function": "__e"
          }],
          "tags": [{
              "function": "__ua",
              "once_per_event": true,
              "vtp_nonInteraction": false,
              "vtp_overrideGaSettings": true,
              "vtp_doubleClick": false,
              "vtp_setTrackerName": false,
              "vtp_useDebugVersion": false,
              "vtp_eventCategory": ["macro", 2],
              "vtp_trackType": "TRACK_EVENT",
              "vtp_enableLinkId": false,
              "vtp_eventAction": ["macro", 3],
              "vtp_eventLabel": ["macro", 4],
              "vtp_enableEcommerce": false,
              "vtp_trackingId": "UA-56956378-19",
              "vtp_enableRecaptchaOption": false,
              "vtp_enableUaRlsa": false,
              "vtp_enableUseInternalVersion": false,
              "vtp_enableFirebaseCampaignData": true,
              "vtp_trackTypeIsEvent": true,
              "vtp_enableGA4Schema": true,
              "tag_id": 1
          }, {
              "function": "__ua",
              "once_per_event": true,
              "vtp_overrideGaSettings": true,
              "vtp_setTrackerName": false,
              "vtp_doubleClick": false,
              "vtp_useDebugVersion": false,
              "vtp_fieldsToSet": ["list", ["map", "fieldName", "userId", "value", ["macro", 6]]],
              "vtp_useHashAutoLink": false,
              "vtp_trackType": "TRACK_PAGEVIEW",
              "vtp_decorateFormsAutoLink": false,
              "vtp_enableLinkId": false,
              "vtp_dimension": ["list", ["map", "index", "1", "dimension", ["macro", 6]]],
              "vtp_enableEcommerce": false,
              "vtp_trackingId": "UA-56956378-19",
              "vtp_enableRecaptchaOption": false,
              "vtp_enableUaRlsa": false,
              "vtp_enableUseInternalVersion": false,
              "vtp_enableFirebaseCampaignData": true,
              "vtp_enableGA4Schema": true,
              "tag_id": 3
          }, {
              "function": "__gaawc",
              "metadata": ["map"],
              "once_per_event": true,
              "vtp_sendPageView": true,
              "vtp_enableSendToServerContainer": false,
              "vtp_measurementId": "G-8PQN6HGTCD",
              "vtp_enableUserProperties": true,
              "vtp_enableEuid": false,
              "tag_id": 16
          }, {
              "function": "__gaawe",
              "metadata": ["map"],
              "once_per_event": true,
              "vtp_sendEcommerceData": false,
              "vtp_eventName": "click_to_casino",
              "vtp_eventParameters": ["list", ["map", "name", "casino_name", "value", ["macro", 4]], ["map", "name", "place", "value", ["macro", 3]]],
              "vtp_measurementId": "G-8PQN6HGTCD",
              "vtp_enableUserProperties": true,
              "vtp_enableMoreSettingsOption": true,
              "vtp_enableEuid": false,
              "vtp_migratedToV2": false,
              "vtp_demoV2": false,
              "tag_id": 20
          }, {
              "function": "__gaawe",
              "metadata": ["map"],
              "once_per_event": true,
              "vtp_sendEcommerceData": false,
              "vtp_eventName": "read_more",
              "vtp_eventParameters": ["list", ["map", "name", "section", "value", ["macro", 4]]],
              "vtp_measurementId": "G-8PQN6HGTCD",
              "vtp_enableUserProperties": true,
              "vtp_enableMoreSettingsOption": true,
              "vtp_enableEuid": false,
              "vtp_migratedToV2": false,
              "vtp_demoV2": false,
              "tag_id": 29
          }, {
              "function": "__gaawe",
              "metadata": ["map"],
              "once_per_event": true,
              "vtp_sendEcommerceData": false,
              "vtp_eventName": ["macro", 7],
              "vtp_eventParameters": ["list", ["map", "name", "game_url", "value", ["macro", 4]]],
              "vtp_measurementId": "G-8PQN6HGTCD",
              "vtp_enableUserProperties": true,
              "vtp_enableMoreSettingsOption": true,
              "vtp_enableEuid": false,
              "vtp_migratedToV2": false,
              "vtp_demoV2": false,
              "tag_id": 30
          }, {
              "function": "__gaawe",
              "metadata": ["map"],
              "once_per_event": true,
              "vtp_sendEcommerceData": false,
              "vtp_eventName": ["macro", 8],
              "vtp_eventParameters": ["list", ["map", "name", "search", "value", ["macro", 4]]],
              "vtp_measurementId": "G-8PQN6HGTCD",
              "vtp_enableUserProperties": true,
              "vtp_enableMoreSettingsOption": true,
              "vtp_enableEuid": false,
              "vtp_migratedToV2": false,
              "vtp_demoV2": false,
              "tag_id": 31
          }, {
              "function": "__gaawe",
              "metadata": ["map"],
              "once_per_event": true,
              "vtp_sendEcommerceData": false,
              "vtp_eventName": ["macro", 9],
              "vtp_measurementId": "G-8PQN6HGTCD",
              "vtp_enableUserProperties": true,
              "vtp_enableMoreSettingsOption": true,
              "vtp_enableEuid": false,
              "vtp_migratedToV2": false,
              "vtp_demoV2": false,
              "tag_id": 32
          }, {
              "function": "__gaawe",
              "metadata": ["map"],
              "once_per_event": true,
              "vtp_sendEcommerceData": false,
              "vtp_eventName": "table_of_content",
              "vtp_eventParameters": ["list", ["map", "name", "content_name", "value", ["macro", 4]]],
              "vtp_measurementId": "G-8PQN6HGTCD",
              "vtp_enableUserProperties": true,
              "vtp_enableMoreSettingsOption": true,
              "vtp_enableEuid": false,
              "vtp_migratedToV2": false,
              "vtp_demoV2": false,
              "tag_id": 33
          }, {
              "function": "__html",
              "metadata": ["map"],
              "unlimited": true,
              "vtp_html": "\u003Cscript type=\"text\/gtmscript\"\u003Ewindow.onload=function(){window.jQuery\u0026\u0026jQuery(document).ready(function(a){a(\"div.toggle-action\").click(function(){var b=a(this).find(\"button\").attr(\"data\");dataLayer.push({event:\"GAevent\",eventCategory:\"Content\",eventAction:\"ReadMore\",eventLabel:\"Section: \"+b})});a(\".menu-small a\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"Content\",eventAction:\"TableOfContent\",eventLabel:a(this).html()})});a(\".toggle-action-menu\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"Content\",\neventAction:\"TableOfContent\",eventLabel:a(this).hasClass(\"opened\")?\"hide\":\"show\"})});a(\".btn-service.fc\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"Panel\",eventAction:\"FullScreen\",eventLabel:\"FullScreen\"})});a(\".btn-service.er\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"Panel\",eventAction:\"IssueReport\",eventLabel:\"IssueReport\"})});a(\".btn-service.yt\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"Panel\",eventAction:\"VideoReview\",eventLabel:\"VideoReview\"})});\na(\"#bookmarkBtn\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"Panel\",eventAction:\"Bookmark\",eventLabel:\"Bookmark\"})});a(\".game-box-similar a\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"GamePageLists\",eventAction:\"UnderGame\",eventLabel:a(this).attr(\"href\")})});a(\".widget_top5games_widget ul li a\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"GamePageLists\",eventAction:\"TopDevGames\",eventLabel:a(this).attr(\"href\")})});a(\".widget_latest_games_widget ul li a\").click(function(){dataLayer.push({event:\"GAevent\",\neventCategory:\"GamePageLists\",eventAction:\"LatestGames\",eventLabel:a(this).attr(\"href\")})});a(\"#casinoBtnTopReview .tc-apply a\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"toCasino\",eventAction:\"TopReviewCasino T\\x26C\",eventLabel:a(this).attr(\"data\")})});a(\"#casinoBtnDownReview .tc-apply a\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"toCasino\",eventAction:\"DownReviewCasino T\\x26C\",eventLabel:a(this).attr(\"data\")})});a(\".widget_single_specification_widget .tc-apply a\").click(function(){dataLayer.push({event:\"GAevent\",\neventCategory:\"toCasino\",eventAction:\"SidebarCasinoDetails T\\x26C\",eventLabel:a(this).attr(\"data\")})});a(\".relevant-casinos ul li a\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"GamePageLists\",eventAction:\"CasinoList\",eventLabel:a(this).attr(\"href\")})});a(\".swu-buttons a\").click(function(){dataLayer.push({event:\"GAevent\",eventCategory:\"Other\",eventAction:\"StandWithUkraine\",eventLabel:\"StandWithUkraine\"})})})};\u003C\/script\u003E\n\n",
              "vtp_supportDocumentWrite": false,
              "vtp_enableIframeMode": false,
              "vtp_enableEditJsMacroBehavior": false,
              "tag_id": 2
          }, {
              "function": "__html",
              "metadata": ["map"],
              "once_per_event": true,
              "vtp_html": "\u003Cscript data-gtmsrc=\"https:\/\/my.rtmark.net\/p.js?f=sync\u0026amp;lr=1\u0026amp;partner=cb85442b280cd8831cdc5911b6f4d7b977a4ef216138d3991c9037cd9b462ea6\" defer type=\"text\/gtmscript\"\u003E\u003C\/script\u003E\n\u003Cnoscript\u003E\u003Cimg src=\"https:\/\/my.rtmark.net\/img.gif?f=sync\u0026amp;lr=1\u0026amp;partner=cb85442b280cd8831cdc5911b6f4d7b977a4ef216138d3991c9037cd9b462ea6\" width=\"1\" height=\"1\"\u003E\u003C\/noscript\u003E",
              "vtp_supportDocumentWrite": false,
              "vtp_enableIframeMode": false,
              "vtp_enableEditJsMacroBehavior": false,
              "tag_id": 15
          }],
          "predicates": [{
              "function": "_cn",
              "arg0": ["macro", 0],
              "arg1": "GAevent"
          }, {
              "function": "_re",
              "arg0": ["macro", 1],
              "arg1": ".*"
          }, {
              "function": "_re",
              "arg0": ["macro", 5],
              "arg1": ".*"
          }, {
              "function": "_eq",
              "arg0": ["macro", 1],
              "arg1": "gtm.js"
          }, {
              "function": "_eq",
              "arg0": ["macro", 2],
              "arg1": "toCasino"
          }, {
              "function": "_eq",
              "arg0": ["macro", 1],
              "arg1": "GAevent"
          }, {
              "function": "_eq",
              "arg0": ["macro", 2],
              "arg1": "Content"
          }, {
              "function": "_eq",
              "arg0": ["macro", 3],
              "arg1": "ReadMore"
          }, {
              "function": "_eq",
              "arg0": ["macro", 2],
              "arg1": "GamePageLists"
          }, {
              "function": "_eq",
              "arg0": ["macro", 2],
              "arg1": "Other"
          }, {
              "function": "_eq",
              "arg0": ["macro", 2],
              "arg1": "Panel"
          }, {
              "function": "_eq",
              "arg0": ["macro", 3],
              "arg1": "TableOfContent"
          }],
          "rules": [[["if", 0, 1], ["add", 0]], [["if", 2, 3], ["add", 1, 2, 9]], [["if", 4, 5], ["add", 3]], [["if", 5, 6, 7], ["add", 4]], [["if", 5, 8], ["add", 5]], [["if", 5, 9], ["add", 6]], [["if", 5, 10], ["add", 7]], [["if", 5, 6, 11], ["add", 8]], [["if", 3], ["add", 10]]]
      },
      "runtime": []

  };

  /*

Copyright The Closure Library Authors.
SPDX-License-Identifier: Apache-2.0
*/
  var ba, ea = function(a) {
      var b = 0;
      return function() {
          return b < a.length ? {
              done: !1,
              value: a[b++]
          } : {
              done: !0
          }
      }
  }, fa = function(a) {
      var b = "undefined" != typeof Symbol && Symbol.iterator && a[Symbol.iterator];
      if (b)
          return b.call(a);
      if ("number" == typeof a.length)
          return {
              next: ea(a)
          };
      throw Error(String(a) + " is not an iterable or ArrayLike");
  }, ia = "function" == typeof Object.create ? Object.create : function(a) {
      var b = function() {};
      b.prototype = a;
      return new b
  }
  , ja;
  if ("function" == typeof Object.setPrototypeOf)
      ja = Object.setPrototypeOf;
  else {
      var ka;
      a: {
          var la = {
              a: !0
          }
            , ma = {};
          try {
              ma.__proto__ = la;
              ka = ma.a;
              break a
          } catch (a) {}
          ka = !1
      }
      ja = ka ? function(a, b) {
          a.__proto__ = b;
          if (a.__proto__ !== b)
              throw new TypeError(a + " is not extensible");
          return a
      }
      : null
  }
  var na = ja
    , oa = function(a, b) {
      a.prototype = ia(b.prototype);
      a.prototype.constructor = a;
      if (na)
          na(a, b);
      else
          for (var c in b)
              if ("prototype" != c)
                  if (Object.defineProperties) {
                      var d = Object.getOwnPropertyDescriptor(b, c);
                      d && Object.defineProperty(a, c, d)
                  } else
                      a[c] = b[c];
      a.lm = b.prototype
  }
    , pa = this || self
    , qa = function(a) {
      return a
  };
  var ra = function() {}
    , sa = function(a) {
      return "function" === typeof a
  }
    , h = function(a) {
      return "string" === typeof a
  }
    , ta = function(a) {
      return "number" === typeof a && !isNaN(a)
  }
    , ua = Array.isArray
    , va = function(a, b) {
      if (a && ua(a))
          for (var c = 0; c < a.length; c++)
              if (a[c] && b(a[c]))
                  return a[c]
  }
    , wa = function(a, b) {
      if (!ta(a) || !ta(b) || a > b)
          a = 0,
          b = 2147483647;
      return Math.floor(Math.random() * (b - a + 1) + a)
  }
    , za = function(a, b) {
      for (var c = new ya, d = 0; d < a.length; d++)
          c.set(a[d], !0);
      for (var e = 0; e < b.length; e++)
          if (c.get(b[e]))
              return !0;
      return !1
  }
    , k = function(a, b) {
      for (var c in a)
          Object.prototype.hasOwnProperty.call(a, c) && b(c, a[c])
  }
    , Aa = function(a) {
      return !!a && ("[object Arguments]" === Object.prototype.toString.call(a) || Object.prototype.hasOwnProperty.call(a, "callee"))
  }
    , Ba = function(a) {
      return Math.round(Number(a)) || 0
  }
    , Da = function(a) {
      return "false" === String(a).toLowerCase() ? !1 : !!a
  }
    , Ea = function(a) {
      var b = [];
      if (ua(a))
          for (var c = 0; c < a.length; c++)
              b.push(String(a[c]));
      return b
  }
    , Fa = function(a) {
      return a ? a.replace(/^\s+|\s+$/g, "") : ""
  }
    , Ga = function() {
      return new Date(Date.now())
  }
    , Ha = function() {
      return Ga().getTime()
  }
    , ya = function() {
      this.prefix = "gtm.";
      this.values = {}
  };
  ya.prototype.set = function(a, b) {
      this.values[this.prefix + a] = b
  }
  ;
  ya.prototype.get = function(a) {
      return this.values[this.prefix + a]
  }
  ;
  var Ia = function(a, b, c) {
      return a && a.hasOwnProperty(b) ? a[b] : c
  }
    , Ja = function(a) {
      var b = a;
      return function() {
          if (b) {
              var c = b;
              b = void 0;
              try {
                  c()
              } catch (d) {}
          }
      }
  }
    , Ka = function(a, b) {
      for (var c in b)
          b.hasOwnProperty(c) && (a[c] = b[c])
  }
    , La = function(a) {
      for (var b in a)
          if (a.hasOwnProperty(b))
              return !0;
      return !1
  }
    , Ma = function(a, b) {
      for (var c = [], d = 0; d < a.length; d++)
          c.push(a[d]),
          c.push.apply(c, b[a[d]] || []);
      return c
  }
    , Na = function(a, b) {
      for (var c = {}, d = c, e = a.split("."), f = 0; f < e.length - 1; f++)
          d = d[e[f]] = {};
      d[e[e.length - 1]] = b;
      return c
  }
    , Oa = /^\w{1,9}$/
    , Qa = function(a, b) {
      a = a || {};
      b = b || ",";
      var c = [];
      k(a, function(d, e) {
          Oa.test(d) && e && c.push(d)
      });
      return c.join(b)
  }
    , Ra = function(a, b) {
      function c() {
          ++d === b && (e(),
          e = null,
          c.done = !0)
      }
      var d = 0
        , e = a;
      c.done = !1;
      return c
  };
  function Sa() {
      for (var a = Ta, b = {}, c = 0; c < a.length; ++c)
          b[a[c]] = c;
      return b
  }
  function Ua() {
      var a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      a += a.toLowerCase() + "0123456789-_";
      return a + "."
  }
  var Ta, Va;
  function Wa(a) {
      Ta = Ta || Ua();
      Va = Va || Sa();
      for (var b = [], c = 0; c < a.length; c += 3) {
          var d = c + 1 < a.length
            , e = c + 2 < a.length
            , f = a.charCodeAt(c)
            , g = d ? a.charCodeAt(c + 1) : 0
            , l = e ? a.charCodeAt(c + 2) : 0
            , m = f >> 2
            , n = (f & 3) << 4 | g >> 4
            , p = (g & 15) << 2 | l >> 6
            , q = l & 63;
          e || (q = 64,
          d || (p = 64));
          b.push(Ta[m], Ta[n], Ta[p], Ta[q])
      }
      return b.join("")
  }
  function Xa(a) {
      function b(m) {
          for (; d < a.length; ) {
              var n = a.charAt(d++)
                , p = Va[n];
              if (null != p)
                  return p;
              if (!/^[\s\xa0]*$/.test(n))
                  throw Error("Unknown base64 encoding at char: " + n);
          }
          return m
      }
      Ta = Ta || Ua();
      Va = Va || Sa();
      for (var c = "", d = 0; ; ) {
          var e = b(-1)
            , f = b(0)
            , g = b(64)
            , l = b(64);
          if (64 === l && -1 === e)
              return c;
          c += String.fromCharCode(e << 2 | f >> 4);
          64 != g && (c += String.fromCharCode(f << 4 & 240 | g >> 2),
          64 != l && (c += String.fromCharCode(g << 6 & 192 | l)))
      }
  }
  ;var Za = {}
    , $a = function(a, b) {
      Za[a] = Za[a] || [];
      Za[a][b] = !0
  }
    , ab = function() {
      delete Za.GA4_EVENT
  }
    , bb = function(a) {
      var b = Za[a];
      if (!b || 0 === b.length)
          return "";
      for (var c = [], d = 0, e = 0; e < b.length; e++)
          0 === e % 8 && 0 < e && (c.push(String.fromCharCode(d)),
          d = 0),
          b[e] && (d |= 1 << e % 8);
      0 < d && c.push(String.fromCharCode(d));
      return Wa(c.join("")).replace(/\.+$/, "")
  };
  var cb = Array.prototype.indexOf ? function(a, b) {
      return Array.prototype.indexOf.call(a, b, void 0)
  }
  : function(a, b) {
      if ("string" === typeof a)
          return "string" !== typeof b || 1 != b.length ? -1 : a.indexOf(b, 0);
      for (var c = 0; c < a.length; c++)
          if (c in a && a[c] === b)
              return c;
      return -1
  }
  ;
  var db, eb = function() {
      if (void 0 === db) {
          var a = null
            , b = pa.trustedTypes;
          if (b && b.createPolicy) {
              try {
                  a = b.createPolicy("goog#html", {
                      createHTML: qa,
                      createScript: qa,
                      createScriptURL: qa
                  })
              } catch (c) {
                  pa.console && pa.console.error(c.message)
              }
              db = a
          } else
              db = a
      }
      return db
  };
  var fb = function(a) {
      this.h = a
  };
  fb.prototype.toString = function() {
      return this.h + ""
  }
  ;
  var gb = {};
  var hb = /^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;
  var ib, jb;
  a: {
      for (var kb = ["CLOSURE_FLAGS"], lb = pa, mb = 0; mb < kb.length; mb++)
          if (lb = lb[kb[mb]],
          null == lb) {
              jb = null;
              break a
          }
      jb = lb
  }
  var nb = jb && jb[610401301];
  ib = null != nb ? nb : !1;
  function ob() {
      var a = pa.navigator;
      if (a) {
          var b = a.userAgent;
          if (b)
              return b
      }
      return ""
  }
  var pb, qb = pa.navigator;
  pb = qb ? qb.userAgentData || null : null;
  function rb(a) {
      return ib ? pb ? pb.brands.some(function(b) {
          var c = b.brand;
          return c && -1 != c.indexOf(a)
      }) : !1 : !1
  }
  function sb(a) {
      return -1 != ob().indexOf(a)
  }
  ;function tb() {
      return ib ? !!pb && 0 < pb.brands.length : !1
  }
  function ub() {
      return tb() ? !1 : sb("Opera")
  }
  function vb() {
      return sb("Firefox") || sb("FxiOS")
  }
  function wb() {
      return tb() ? rb("Chromium") : (sb("Chrome") || sb("CriOS")) && !(tb() ? 0 : sb("Edge")) || sb("Silk")
  }
  ;var xb = {}
    , yb = function(a) {
      this.h = a
  };
  yb.prototype.toString = function() {
      return this.h.toString()
  }
  ;
  var zb = function(a) {
      return a instanceof yb && a.constructor === yb ? a.h : "type_error:SafeHtml"
  };
  /*

SPDX-License-Identifier: Apache-2.0
*/
  function Ab(a) {
      var b = a.tagName;
      if ("SCRIPT" === b || "STYLE" === b)
          throw Error("");
  }
  ;(function() {
      return ""
  }
  ).toString().indexOf("`");
  function Bb(a) {
      var b = a = Cb(a)
        , c = eb()
        , d = c ? c.createHTML(b) : b;
      return new yb(d,xb)
  }
  function Cb(a) {
      return null === a ? "null" : void 0 === a ? "undefined" : a
  }
  ;var z = window
    , C = document
    , Db = navigator
    , Fb = C.currentScript && C.currentScript.src
    , Gb = function(a, b) {
      var c = z[a];
      z[a] = void 0 === c ? b : c;
      return z[a]
  }
    , Hb = function(a, b) {
      b && (a.addEventListener ? a.onload = b : a.onreadystatechange = function() {
          a.readyState in {
              loaded: 1,
              complete: 1
          } && (a.onreadystatechange = null,
          b())
      }
      )
  }
    , Ib = {
      async: 1,
      nonce: 1,
      onerror: 1,
      onload: 1,
      src: 1,
      type: 1
  }
    , Jb = {
      onload: 1,
      src: 1,
      width: 1,
      height: 1,
      style: 1
  };
  function Kb(a, b, c) {
      b && k(b, function(d, e) {
          d = d.toLowerCase();
          c.hasOwnProperty(d) || a.setAttribute(d, e)
      })
  }
  var Lb = function(a, b, c, d, e) {
      var f = C.createElement("script");
      Kb(f, d, Ib);
      f.type = "text/javascript";
      f.async = !0;
      var g, l = Cb(a), m = eb(), n = m ? m.createScriptURL(l) : l;
      g = new fb(n,gb);
      f.src = g instanceof fb && g.constructor === fb ? g.h : "type_error:TrustedResourceUrl";
      var p, q, r, t = null == (r = (q = (f.ownerDocument && f.ownerDocument.defaultView || window).document).querySelector) ? void 0 : r.call(q, "script[nonce]");
      (p = t ? t.nonce || t.getAttribute("nonce") || "" : "") && f.setAttribute("nonce", p);
      Hb(f, b);
      c && (f.onerror = c);
      if (e)
          e.appendChild(f);
      else {
          var u = C.getElementsByTagName("script")[0] || C.body || C.head;
          u.parentNode.insertBefore(f, u)
      }
      return f
  }
    , Mb = function() {
      if (Fb) {
          var a = Fb.toLowerCase();
          if (0 === a.indexOf("https://"))
              return 2;
          if (0 === a.indexOf("http://"))
              return 3
      }
      return 1
  }
    , Nb = function(a, b, c, d, e) {
      var f;
      f = void 0 === f ? !0 : f;
      var g = e
        , l = !1;
      g || (g = C.createElement("iframe"),
      l = !0);
      Kb(g, c, Jb);
      d && k(d, function(n, p) {
          g.dataset[n] = p
      });
      f && (g.height = "0",
      g.width = "0",
      g.style.display = "none",
      g.style.visibility = "hidden");
      if (l) {
          var m = C.body && C.body.lastChild || C.body || C.head;
          m.parentNode.insertBefore(g, m)
      }
      Hb(g, b);
      void 0 !== a && (g.src = a);
      return g
  }
    , Ob = function(a, b, c, d) {
      var e = new Image(1,1);
      Kb(e, d, {});
      e.onload = function() {
          e.onload = null;
          b && b()
      }
      ;
      e.onerror = function() {
          e.onerror = null;
          c && c()
      }
      ;
      e.src = a
  }
    , Pb = function(a, b, c, d) {
      a.addEventListener ? a.addEventListener(b, c, !!d) : a.attachEvent && a.attachEvent("on" + b, c)
  }
    , Qb = function(a, b, c) {
      a.removeEventListener ? a.removeEventListener(b, c, !1) : a.detachEvent && a.detachEvent("on" + b, c)
  }
    , F = function(a) {
      z.setTimeout(a, 0)
  }
    , Rb = function(a, b) {
      return a && b && a.attributes && a.attributes[b] ? a.attributes[b].value : null
  }
    , Sb = function(a) {
      var b = a.innerText || a.textContent || "";
      b && " " != b && (b = b.replace(/^[\s\xa0]+|[\s\xa0]+$/g, ""));
      b && (b = b.replace(/(\xa0+|\s{2,}|\n|\r\t)/g, " "));
      return b
  }
    , Tb = function(a) {
      var b = C.createElement("div")
        , c = b
        , d = Bb("A<div>" + a + "</div>");
      1 === c.nodeType && Ab(c);
      c.innerHTML = zb(d);
      b = b.lastChild;
      for (var e = []; b.firstChild; )
          e.push(b.removeChild(b.firstChild));
      return e
  }
    , Ub = function(a, b, c) {
      c = c || 100;
      for (var d = {}, e = 0; e < b.length; e++)
          d[b[e]] = !0;
      for (var f = a, g = 0; f && g <= c; g++) {
          if (d[String(f.tagName).toLowerCase()])
              return f;
          f = f.parentElement
      }
      return null
  }
    , Vb = function(a) {
      var b;
      try {
          b = Db.sendBeacon && Db.sendBeacon(a)
      } catch (c) {
          $a("TAGGING", 15)
      }
      b || Ob(a)
  }
    , Wb = function(a, b) {
      var c = a[b];
      c && "string" === typeof c.animVal && (c = c.animVal);
      return c
  }
    , Xb = function(a, b) {
      try {
          z.fetch(a, b)
      } catch (c) {}
  }
    , Yb = function() {
      var a = z.performance;
      if (a && sa(a.now))
          return a.now()
  }
    , Zb = function() {
      return z.performance || void 0
  };
  /*
jQuery (c) 2005, 2012 jQuery Foundation, Inc. jquery.org/license. */
  var $b = /\[object (Boolean|Number|String|Function|Array|Date|RegExp)\]/
    , ac = function(a) {
      if (null == a)
          return String(a);
      var b = $b.exec(Object.prototype.toString.call(Object(a)));
      return b ? b[1].toLowerCase() : "object"
  }
    , bc = function(a, b) {
      return Object.prototype.hasOwnProperty.call(Object(a), b)
  }
    , G = function(a) {
      if (!a || "object" != ac(a) || a.nodeType || a == a.window)
          return !1;
      try {
          if (a.constructor && !bc(a, "constructor") && !bc(a.constructor.prototype, "isPrototypeOf"))
              return !1
      } catch (c) {
          return !1
      }
      for (var b in a)
          ;
      return void 0 === b || bc(a, b)
  }
    , J = function(a, b) {
      var c = b || ("array" == ac(a) ? [] : {}), d;
      for (d in a)
          if (bc(a, d)) {
              var e = a[d];
              "array" == ac(e) ? ("array" != ac(c[d]) && (c[d] = []),
              c[d] = J(e, c[d])) : G(e) ? (G(c[d]) || (c[d] = {}),
              c[d] = J(e, c[d])) : c[d] = e
          }
      return c
  };
  var cc = function(a) {
      if (void 0 === a || ua(a) || G(a))
          return !0;
      switch (typeof a) {
      case "boolean":
      case "number":
      case "string":
      case "function":
          return !0
      }
      return !1
  };
  function dc(a) {
      switch (a) {
      case 1:
          return "1";
      case 2:
      case 4:
          return "0";
      default:
          return "-"
      }
  }
  function ec(a) {
      switch (a) {
      case 1:
          return "G";
      case 3:
          return "g";
      case 2:
          return "D";
      case 4:
          return "d";
      case 0:
          return "g";
      default:
          return "g"
      }
  }
  function fc(a, b) {
      var c = a[1] || 0
        , d = a[2] || 0
        , e = a[3] || 0
        , f = a[4] || 0;
      switch (b) {
      case 0:
          return "G1" + dc(c) + dc(d);
      case 1:
          return "G2" + ec(c) + ec(d);
      case 2:
          return "G2" + ec(c) + ec(d) + ec(e) + ec(f);
      default:
          return "g1--"
      }
  }
  ;var gc = function() {
      var a = function(b) {
          return {
              toString: function() {
                  return b
              }
          }
      };
      return {
          Ii: a("consent"),
          Fg: a("convert_case_to"),
          Gg: a("convert_false_to"),
          Hg: a("convert_null_to"),
          Ig: a("convert_true_to"),
          Jg: a("convert_undefined_to"),
          Ml: a("debug_mode_metadata"),
          zb: a("function"),
          If: a("instance_name"),
          Kj: a("live_only"),
          Lj: a("malware_disabled"),
          Mj: a("metadata"),
          Pj: a("original_activity_id"),
          Ul: a("original_vendor_template_id"),
          Tl: a("once_on_load"),
          Oj: a("once_per_event"),
          Jh: a("once_per_load"),
          Yl: a("priority_override"),
          Zl: a("respected_consent_types"),
          Nh: a("setup_tags"),
          ud: a("tag_id"),
          Sh: a("teardown_tags")
      }
  }();
  var Dc;
  var Ec = [], Fc = [], Gc = [], Hc = [], Ic = [], Jc = {}, Kc, Lc, Nc = function() {
      var a = Mc;
      Lc = Lc || a
  }, Oc, Pc = [], Qc = function(a, b) {
      var c = a["function"]
        , d = b && b.event;
      if (!c)
          throw Error("Error: No function name given for function call.");
      var e = Jc[c], f = b && 2 === b.type && d.vi && e && -1 !== Pc.indexOf(c), g = {}, l = {}, m;
      for (m in a)
          a.hasOwnProperty(m) && 0 === m.indexOf("vtp_") && (e && d && d.Xh && d.Xh(a[m]),
          e && (g[m] = a[m]),
          !e || f) && (l[m.substr(4)] = a[m]);
      e && d && d.Wh && (g.vtp_gtmCachedValues = d.Wh);
      if (b) {
          if (null == b.name) {
              var n;
              a: {
                  var p = b.index;
                  if (null == p)
                      n = "";
                  else {
                      var q;
                      switch (b.type) {
                      case 2:
                          q = Ec[p];
                          break;
                      case 1:
                          q = Hc[p];
                          break;
                      default:
                          n = "";
                          break a
                      }
                      var r = q && q[gc.If];
                      n = r ? String(r) : ""
                  }
              }
              b.name = n
          }
          e && (g.vtp_gtmEntityIndex = b.index,
          g.vtp_gtmEntityName = b.name)
      }
      var t, u;
      e && (t = e(g));
      if (!e || f)
          u = Dc(c, l, b);
      f && t !== u && d && d.vi(d.id, c);
      return e ? t : u
  }, Sc = function(a, b, c) {
      c = c || [];
      var d = {}, e;
      for (e in a)
          a.hasOwnProperty(e) && (d[e] = Rc(a[e], b, c));
      return d
  }, Rc = function(a, b, c) {
      if (ua(a)) {
          var d;
          switch (a[0]) {
          case "function_id":
              return a[1];
          case "list":
              d = [];
              for (var e = 1; e < a.length; e++)
                  d.push(Rc(a[e], b, c));
              return d;
          case "macro":
              var f = a[1];
              if (c[f])
                  return;
              var g = Ec[f];
              if (!g || b.Yf(g))
                  return;
              c[f] = !0;
              var l = String(g[gc.If]);
              try {
                  var m = Sc(g, b, c);
                  m.vtp_gtmEventId = b.id;
                  b.priorityId && (m.vtp_gtmPriorityId = b.priorityId);
                  d = Qc(m, {
                      event: b,
                      index: f,
                      type: 2,
                      name: l
                  });
                  Oc && (d = Oc.ek(d, m))
              } catch (y) {
                  b.ji && b.ji(y, Number(f), l),
                  d = !1
              }
              c[f] = !1;
              return d;
          case "map":
              d = {};
              for (var n = 1; n < a.length; n += 2)
                  d[Rc(a[n], b, c)] = Rc(a[n + 1], b, c);
              return d;
          case "template":
              d = [];
              for (var p = !1, q = 1; q < a.length; q++) {
                  var r = Rc(a[q], b, c);
                  Lc && (p = p || r === Lc.Be);
                  d.push(r)
              }
              return Lc && p ? Lc.fk(d) : d.join("");
          case "escape":
              d = Rc(a[1], b, c);
              if (Lc && ua(a[1]) && "macro" === a[1][0] && Lc.Ik(a))
                  return Lc.il(d);
              d = String(d);
              for (var t = 2; t < a.length; t++)
                  hc[a[t]] && (d = hc[a[t]](d));
              return d;
          case "tag":
              var u = a[1];
              if (!Hc[u])
                  throw Error("Unable to resolve tag reference " + u + ".");
              return d = {
                  di: a[2],
                  index: u
              };
          case "zb":
              var v = {
                  arg0: a[2],
                  arg1: a[3],
                  ignore_case: a[5]
              };
              v["function"] = a[1];
              var w = Tc(v, b, c)
                , x = !!a[4];
              return x || 2 !== w ? x !== (1 === w) : null;
          default:
              throw Error("Attempting to expand unknown Value type: " + a[0] + ".");
          }
      }
      return a
  }, Tc = function(a, b, c) {
      try {
          return Kc(Sc(a, b, c))
      } catch (d) {
          JSON.stringify(a)
      }
      return 2
  };
  var Wc = function(a) {
      function b(r) {
          for (var t = 0; t < r.length; t++)
              d[r[t]] = !0
      }
      for (var c = [], d = [], e = Uc(a), f = 0; f < Fc.length; f++) {
          var g = Fc[f]
            , l = Vc(g, e);
          if (l) {
              for (var m = g.add || [], n = 0; n < m.length; n++)
                  c[m[n]] = !0;
              b(g.block || [])
          } else
              null === l && b(g.block || []);
      }
      for (var p = [], q = 0; q < Hc.length; q++)
          c[q] && !d[q] && (p[q] = !0);
      return p
  }
    , Vc = function(a, b) {
      for (var c = a["if"] || [], d = 0; d < c.length; d++) {
          var e = b(c[d]);
          if (0 === e)
              return !1;
          if (2 === e)
              return null
      }
      for (var f = a.unless || [], g = 0; g < f.length; g++) {
          var l = b(f[g]);
          if (2 === l)
              return null;
          if (1 === l)
              return !1
      }
      return !0
  }
    , Uc = function(a) {
      var b = [];
      return function(c) {
          void 0 === b[c] && (b[c] = Tc(Gc[c], a));
          return b[c]
      }
  };
  var Xc = {
      ek: function(a, b) {
          b[gc.Fg] && "string" === typeof a && (a = 1 == b[gc.Fg] ? a.toLowerCase() : a.toUpperCase());
          b.hasOwnProperty(gc.Hg) && null === a && (a = b[gc.Hg]);
          b.hasOwnProperty(gc.Jg) && void 0 === a && (a = b[gc.Jg]);
          b.hasOwnProperty(gc.Ig) && !0 === a && (a = b[gc.Ig]);
          b.hasOwnProperty(gc.Gg) && !1 === a && (a = b[gc.Gg]);
          return a
      }
  };
  var kd = ["matches", "webkitMatchesSelector", "mozMatchesSelector", "msMatchesSelector", "oMatchesSelector"];
  function ld(a, b) {
      a = String(a);
      b = String(b);
      var c = a.length - b.length;
      return 0 <= c && a.indexOf(b, c) === c
  }
  var md = new ya;
  function nd(a, b, c) {
      var d = c ? "i" : void 0;
      try {
          var e = String(b) + d
            , f = md.get(e);
          f || (f = new RegExp(b,d),
          md.set(e, f));
          return f.test(a)
      } catch (g) {
          return !1
      }
  }
  ;var ud = /^[1-9a-zA-Z_-][1-9a-c][1-9a-v]\d$/;
  function vd(a, b) {
      return "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"[a << 2 | b]
  }
  ;var xd = function(a) {
      return wd ? C.querySelectorAll(a) : null
  }
    , yd = function(a, b) {
      if (!wd)
          return null;
      if (Element.prototype.closest)
          try {
              return a.closest(b)
          } catch (e) {
              return null
          }
      var c = Element.prototype.matches || Element.prototype.webkitMatchesSelector || Element.prototype.mozMatchesSelector || Element.prototype.msMatchesSelector || Element.prototype.oMatchesSelector
        , d = a;
      if (!C.documentElement.contains(d))
          return null;
      do {
          try {
              if (c.call(d, b))
                  return d
          } catch (e) {
              break
          }
          d = d.parentElement || d.parentNode
      } while (null !== d && 1 === d.nodeType);
      return null
  }
    , zd = !1;
  if (C.querySelectorAll)
      try {
          var Cd = C.querySelectorAll(":root");
          Cd && 1 == Cd.length && Cd[0] == C.documentElement && (zd = !0)
      } catch (a) {}
  var wd = zd;
  var K = function(a) {
      $a("GTM", a)
  };
  var N = {
      g: {
          cf: "ad_data_sharing",
          D: "ad_storage",
          Vd: "ad_user_data",
          M: "analytics_storage",
          Xb: "region",
          Wd: "consent_updated",
          Bg: "wait_for_update",
          Mi: "ads",
          Ll: "all",
          Ni: "play",
          Oi: "search",
          Pi: "youtube",
          Qi: "app_remove",
          Ri: "app_store_refund",
          Si: "app_store_subscription_cancel",
          Ti: "app_store_subscription_convert",
          Ui: "app_store_subscription_renew",
          Kg: "add_payment_info",
          Lg: "add_shipping_info",
          Yb: "add_to_cart",
          Zb: "remove_from_cart",
          Mg: "view_cart",
          Cb: "begin_checkout",
          ac: "select_item",
          Va: "view_item_list",
          pb: "select_promotion",
          Wa: "view_promotion",
          Ca: "purchase",
          bc: "refund",
          Da: "view_item",
          Ng: "add_to_wishlist",
          Vi: "exception",
          Wi: "first_open",
          Xi: "first_visit",
          ja: "gtag.config",
          Ea: "gtag.get",
          Yi: "in_app_purchase",
          fc: "page_view",
          Zi: "screen_view",
          aj: "session_start",
          bj: "timing_complete",
          cj: "track_social",
          Yd: "user_engagement",
          qb: "gclid",
          ka: "ads_data_redaction",
          T: "allow_ad_personalization_signals",
          Zd: "allow_custom_scripts",
          jf: "allow_display_features",
          ae: "allow_enhanced_conversions",
          rb: "allow_google_signals",
          ya: "allow_interest_groups",
          dj: "app_id",
          ej: "app_installer_id",
          fj: "app_name",
          gj: "app_version",
          hc: "auid",
          ij: "auto_detection_enabled",
          Db: "aw_remarketing",
          kf: "aw_remarketing_only",
          be: "discount",
          ce: "aw_feed_country",
          de: "aw_feed_language",
          U: "items",
          ee: "aw_merchant_id",
          Og: "aw_basket_type",
          Lc: "campaign_content",
          Mc: "campaign_id",
          Nc: "campaign_medium",
          Oc: "campaign_name",
          Pc: "campaign",
          Qc: "campaign_source",
          Rc: "campaign_term",
          Xa: "client_id",
          jj: "content_group",
          kj: "content_type",
          Fa: "conversion_cookie_prefix",
          Sc: "conversion_id",
          ra: "conversion_linker",
          Eb: "conversion_api",
          Ja: "cookie_domain",
          za: "cookie_expires",
          Ka: "cookie_flags",
          ic: "cookie_name",
          Tc: "cookie_path",
          Ga: "cookie_prefix",
          Za: "cookie_update",
          sb: "country",
          oa: "currency",
          fe: "customer_lifetime_value",
          jc: "custom_map",
          Pg: "gcldc",
          lj: "debug_mode",
          V: "developer_id",
          mj: "disable_merchant_reported_purchases",
          kc: "dc_custom_params",
          Qg: "dc_natural_search",
          lf: "dynamic_event_settings",
          Rg: "affiliation",
          he: "checkout_option",
          nf: "checkout_step",
          Sg: "coupon",
          Uc: "item_list_name",
          pf: "list_name",
          nj: "promotions",
          Vc: "shipping",
          qf: "tax",
          ie: "engagement_time_msec",
          Wc: "enhanced_client_id",
          Xc: "enhanced_conversions",
          Tg: "enhanced_conversions_automatic_settings",
          je: "estimated_delivery_date",
          rf: "euid_logged_in_state",
          mc: "event_callback",
          oj: "event_category",
          tb: "event_developer_id_string",
          pj: "event_label",
          Ug: "event",
          ke: "event_settings",
          me: "event_timeout",
          qj: "description",
          rj: "fatal",
          sj: "experiments",
          tf: "firebase_id",
          ne: "first_party_collection",
          oe: "_x_20",
          Fb: "_x_19",
          Vg: "fledge",
          Wg: "flight_error_code",
          Xg: "flight_error_message",
          Yg: "fl_activity_category",
          Zg: "fl_activity_group",
          uf: "fl_advertiser_id",
          ah: "fl_ar_dedupe",
          bh: "fl_random_number",
          eh: "tran",
          fh: "u",
          pe: "gac_gclid",
          nc: "gac_wbraid",
          gh: "gac_wbraid_multiple_conversions",
          hh: "ga_restrict_domain",
          vf: "ga_temp_client_id",
          qe: "gdpr_applies",
          ih: "geo_granularity",
          ab: "value_callback",
          La: "value_key",
          Ol: "google_ono",
          cb: "google_signals",
          jh: "google_tld",
          se: "groups",
          kh: "gsa_experiment_id",
          lh: "iframe_state",
          te: "ignore_referrer",
          wf: "internal_traffic_results",
          Gb: "is_legacy_converted",
          vb: "is_legacy_loaded",
          ue: "is_passthrough",
          sa: "language",
          xf: "legacy_developer_id_string",
          wa: "linker",
          oc: "accept_incoming",
          wb: "decorate_forms",
          N: "domains",
          Hb: "url_position",
          mh: "method",
          tj: "name",
          Yc: "new_customer",
          nh: "non_interaction",
          uj: "optimize_id",
          yf: "page_hostname",
          Ib: "page_path",
          Aa: "page_referrer",
          xb: "page_title",
          oh: "passengers",
          ph: "phone_conversion_callback",
          vj: "phone_conversion_country_code",
          qh: "phone_conversion_css_class",
          wj: "phone_conversion_ids",
          rh: "phone_conversion_number",
          sh: "phone_conversion_options",
          qc: "quantity",
          Zc: "redact_device_info",
          zf: "redact_enhanced_user_id",
          xj: "redact_ga_client_id",
          yj: "redact_user_id",
          ve: "referral_exclusion_definition",
          Jb: "restricted_data_processing",
          zj: "retoken",
          Aj: "sample_rate",
          Af: "screen_name",
          yb: "screen_resolution",
          Bj: "search_term",
          Ma: "send_page_view",
          Kb: "send_to",
          we: "server_container_url",
          ad: "session_duration",
          xe: "session_engaged",
          Bf: "session_engaged_time",
          eb: "session_id",
          ye: "session_number",
          bd: "delivery_postal_code",
          th: "temporary_client_id",
          Cf: "topmost_url",
          Cj: "tracking_id",
          Df: "traffic_type",
          la: "transaction_id",
          sc: "transport_url",
          uh: "trip_type",
          dd: "update",
          fb: "url_passthrough",
          ed: "_user_agent_architecture",
          fd: "_user_agent_bitness",
          gd: "_user_agent_full_version_list",
          hd: "_user_agent_mobile",
          jd: "_user_agent_model",
          kd: "_user_agent_platform",
          ld: "_user_agent_platform_version",
          md: "_user_agent_wow64",
          ma: "user_data",
          vh: "user_data_auto_latency",
          wh: "user_data_auto_meta",
          xh: "user_data_auto_multi",
          yh: "user_data_auto_selectors",
          zh: "user_data_auto_status",
          Ef: "user_data_mode",
          Ff: "user_data_settings",
          xa: "user_id",
          Na: "user_properties",
          Ah: "us_privacy_string",
          Z: "value",
          uc: "wbraid",
          Bh: "wbraid_multiple_conversions",
          Gh: "_host_name",
          Hh: "_in_page_command",
          Ih: "_is_passthrough_cid",
          De: "non_personalized_ads",
          sd: "_sst_parameters",
          Ya: "conversion_label",
          fa: "page_location",
          ub: "global_developer_id_string",
          ze: "tc_privacy_string"
      }
  }
    , $d = {}
    , ae = Object.freeze(($d[N.g.T] = 1,
  $d[N.g.jf] = 1,
  $d[N.g.ae] = 1,
  $d[N.g.rb] = 1,
  $d[N.g.U] = 1,
  $d[N.g.Ja] = 1,
  $d[N.g.za] = 1,
  $d[N.g.Ka] = 1,
  $d[N.g.ic] = 1,
  $d[N.g.Tc] = 1,
  $d[N.g.Ga] = 1,
  $d[N.g.Za] = 1,
  $d[N.g.jc] = 1,
  $d[N.g.V] = 1,
  $d[N.g.lf] = 1,
  $d[N.g.mc] = 1,
  $d[N.g.ke] = 1,
  $d[N.g.me] = 1,
  $d[N.g.ne] = 1,
  $d[N.g.hh] = 1,
  $d[N.g.cb] = 1,
  $d[N.g.jh] = 1,
  $d[N.g.se] = 1,
  $d[N.g.wf] = 1,
  $d[N.g.Gb] = 1,
  $d[N.g.vb] = 1,
  $d[N.g.wa] = 1,
  $d[N.g.zf] = 1,
  $d[N.g.ve] = 1,
  $d[N.g.Jb] = 1,
  $d[N.g.Ma] = 1,
  $d[N.g.Kb] = 1,
  $d[N.g.we] = 1,
  $d[N.g.ad] = 1,
  $d[N.g.Bf] = 1,
  $d[N.g.bd] = 1,
  $d[N.g.sc] = 1,
  $d[N.g.dd] = 1,
  $d[N.g.Ff] = 1,
  $d[N.g.Na] = 1,
  $d[N.g.sd] = 1,
  $d));
  Object.freeze([N.g.fa, N.g.Aa, N.g.xb, N.g.sa, N.g.Af, N.g.xa, N.g.tf, N.g.jj]);
  var be = {}
    , ce = Object.freeze((be[N.g.Qi] = 1,
  be[N.g.Ri] = 1,
  be[N.g.Si] = 1,
  be[N.g.Ti] = 1,
  be[N.g.Ui] = 1,
  be[N.g.Wi] = 1,
  be[N.g.Xi] = 1,
  be[N.g.Yi] = 1,
  be[N.g.aj] = 1,
  be[N.g.Yd] = 1,
  be))
    , de = {}
    , ee = Object.freeze((de[N.g.Kg] = 1,
  de[N.g.Lg] = 1,
  de[N.g.Yb] = 1,
  de[N.g.Zb] = 1,
  de[N.g.Mg] = 1,
  de[N.g.Cb] = 1,
  de[N.g.ac] = 1,
  de[N.g.Va] = 1,
  de[N.g.pb] = 1,
  de[N.g.Wa] = 1,
  de[N.g.Ca] = 1,
  de[N.g.bc] = 1,
  de[N.g.Da] = 1,
  de[N.g.Ng] = 1,
  de))
    , fe = Object.freeze([N.g.T, N.g.rb, N.g.Za])
    , ge = Object.freeze([].concat(fe))
    , he = Object.freeze([N.g.za, N.g.me, N.g.ad, N.g.Bf, N.g.ie])
    , ie = Object.freeze([].concat(he))
    , je = {}
    , ke = (je[N.g.D] = "1",
  je[N.g.M] = "2",
  je)
    , le = {}
    , me = Object.freeze((le[N.g.T] = 1,
  le[N.g.ae] = 1,
  le[N.g.ya] = 1,
  le[N.g.Db] = 1,
  le[N.g.kf] = 1,
  le[N.g.be] = 1,
  le[N.g.ce] = 1,
  le[N.g.de] = 1,
  le[N.g.U] = 1,
  le[N.g.ee] = 1,
  le[N.g.Fa] = 1,
  le[N.g.ra] = 1,
  le[N.g.Ja] = 1,
  le[N.g.za] = 1,
  le[N.g.Ka] = 1,
  le[N.g.Ga] = 1,
  le[N.g.oa] = 1,
  le[N.g.fe] = 1,
  le[N.g.V] = 1,
  le[N.g.mj] = 1,
  le[N.g.Xc] = 1,
  le[N.g.je] = 1,
  le[N.g.tf] = 1,
  le[N.g.ne] = 1,
  le[N.g.Gb] = 1,
  le[N.g.vb] = 1,
  le[N.g.sa] = 1,
  le[N.g.Yc] = 1,
  le[N.g.fa] = 1,
  le[N.g.Aa] = 1,
  le[N.g.ph] = 1,
  le[N.g.qh] = 1,
  le[N.g.rh] = 1,
  le[N.g.sh] = 1,
  le[N.g.Jb] = 1,
  le[N.g.Ma] = 1,
  le[N.g.Kb] = 1,
  le[N.g.we] = 1,
  le[N.g.bd] = 1,
  le[N.g.la] = 1,
  le[N.g.sc] = 1,
  le[N.g.dd] = 1,
  le[N.g.fb] = 1,
  le[N.g.ma] = 1,
  le[N.g.xa] = 1,
  le[N.g.Z] = 1,
  le));
  Object.freeze(N.g);
  var ne = {}
    , oe = z.google_tag_manager = z.google_tag_manager || {}
    , qe = Math.random();
  ne.Kf = "35v0";
  ne.rd = Number("0") || 0;
  ne.da = "dataLayer";
  ne.Ki = "ChEI8IPhowYQpcLj862U47OvARIkAOTrFH0gDIxmZyyZFI+x1JpbxdHjMLjgg8FlcEhk2kGitOJVGgISjQ\x3d\x3d";
  var re = {
      __cl: 1,
      __ecl: 1,
      __ehl: 1,
      __evl: 1,
      __fal: 1,
      __fil: 1,
      __fsl: 1,
      __hl: 1,
      __jel: 1,
      __lcl: 1,
      __sdl: 1,
      __tl: 1,
      __ytl: 1
  }, se = {
      __paused: 1,
      __tg: 1
  }, te;
  for (te in re)
      re.hasOwnProperty(te) && (se[te] = 1);
  var ue = Da(""), ve, we = !1;
  ve = we;
  var xe, ye = !1;
  xe = ye;
  var ze, Ae = !1;
  ze = Ae;
  var Be, Ce = !1;
  Be = Ce;
  ne.Xd = "www.googletagmanager.com";
  var De = "" + ne.Xd + (ve ? "/gtag/js" : "/gtm.js")
    , Ee = null
    , Fe = null
    , Ge = {}
    , He = {}
    , Ie = {}
    , Je = function() {
      var a = oe.sequence || 1;
      oe.sequence = a + 1;
      return a
  };
  ne.Ji = "";
  var Ke = "";
  ne.He = Ke;
  var Le = new ya
    , Me = {}
    , Ne = {}
    , Qe = {
      name: ne.da,
      set: function(a, b) {
          J(Na(a, b), Me);
          Oe()
      },
      get: function(a) {
          return Pe(a, 2)
      },
      reset: function() {
          Le = new ya;
          Me = {};
          Oe()
      }
  }
    , Pe = function(a, b) {
      return 2 != b ? Le.get(a) : Re(a)
  }
    , Re = function(a) {
      var b, c = a.split(".");
      b = b || [];
      for (var d = Me, e = 0; e < c.length; e++) {
          if (null === d)
              return !1;
          if (void 0 === d)
              break;
          d = d[c[e]];
          if (-1 !== b.indexOf(d))
              return
      }
      return d
  }
    , Se = function(a, b) {
      Ne.hasOwnProperty(a) || (Le.set(a, b),
      J(Na(a, b), Me),
      Oe())
  }
    , Oe = function(a) {
      k(Ne, function(b, c) {
          Le.set(b, c);
          J(Na(b), Me);
          J(Na(b, c), Me);
          a && delete Ne[b]
      })
  }
    , Te = function(a, b) {
      var c, d = 1 !== (void 0 === b ? 2 : b) ? Re(a) : Le.get(a);
      "array" === ac(d) || "object" === ac(d) ? c = J(d) : c = d;
      return c
  };
  var Ue = []
    , Ve = function(a) {
      return void 0 == Ue[a] ? !1 : Ue[a]
  };
  var O = [];
  O[7] = !0;
  O[9] = !0;
  O[27] = !0;
  O[28] = !0;
  O[11] = !0;
  O[13] = !0;
  O[55] = !0;
  O[15] = !0;
  O[16] = !0;
  O[25] = !0;
  O[26] = !0;
  O[34] = !0;
  O[36] = !0;
  O[43] = !0;
  O[52] = !0;
  O[57] = !0;
  O[59] = !0;
  O[61] = !0;

  O[68] = !0;
  O[72] = !0;
  O[73] = !0,
  Ue[1] = !0;
  O[75] = !0;
  Ue[2] = !0;
  O[76] = !0;
  O[77] = !0;
  O[79] = !0;
  O[80] = !0;
  O[83] = !0;
  O[88] = !0;
  O[89] = !0;
  O[92] = !0;
  O[93] = !0;
  O[94] = !0;
  O[96] = !0;
  O[97] = !0;
  O[113] = !0;
  O[115] = !0;
  var R = function(a) {
      return !!O[a]
  };
  var We;
  try {
      We = JSON.parse(Xa("eyIwIjoiVVMiLCIxIjoiVVMtTkoiLCIyIjpmYWxzZSwiMyI6IiIsIjQiOiIiLCI1Ijp0cnVlLCI2IjpmYWxzZSwiNyI6IiJ9"))
  } catch (a) {
      K(123),
      $a("HEALTH", 2),
      We = {}
  }
  var Xe = function() {
      var a = !1;
      return a
  }
    , Ye = function() {
      return !!We["6"]
  }
    , Ze = function() {
      var a = "";
      return a
  }
    , $e = function() {
      var a = !1;
      return a
  }
    , af = function() {
      var a = "";
      return a
  };
  var bf, cf = !1, df = function(a) {
      if (!cf) {
          cf = !0;
          bf = bf || {}
      }
      return bf[a]
  };
  var ef = function() {
      var a = z.screen;
      return {
          width: a ? a.width : 0,
          height: a ? a.height : 0
      }
  }
    , ff = function(a) {
      if (C.hidden)
          return !0;
      var b = a.getBoundingClientRect();
      if (b.top == b.bottom || b.left == b.right || !z.getComputedStyle)
          return !0;
      var c = z.getComputedStyle(a, null);
      if ("hidden" === c.visibility)
          return !0;
      for (var d = a, e = c; d; ) {
          if ("none" === e.display)
              return !0;
          var f = e.opacity
            , g = e.filter;
          if (g) {
              var l = g.indexOf("opacity(");
              0 <= l && (g = g.substring(l + 8, g.indexOf(")", l)),
              "%" == g.charAt(g.length - 1) && (g = g.substring(0, g.length - 1)),
              f = Math.min(g, f))
          }
          if (void 0 !== f && 0 >= f)
              return !0;
          (d = d.parentElement) && (e = z.getComputedStyle(d, null))
      }
      return !1
  };
  var sf = /:[0-9]+$/
    , tf = /^\d+\.fls\.doubleclick\.net$/
    , uf = function(a, b, c) {
      for (var d = a.split("&"), e = 0; e < d.length; e++) {
          var f = d[e].split("=");
          if (decodeURIComponent(f[0]).replace(/\+/g, " ") === b) {
              var g = f.slice(1).join("=");
              return c ? g : decodeURIComponent(g).replace(/\+/g, " ")
          }
      }
  }
    , xf = function(a, b, c, d, e) {
      b && (b = String(b).toLowerCase());
      if ("protocol" === b || "port" === b)
          a.protocol = vf(a.protocol) || vf(z.location.protocol);
      "port" === b ? a.port = String(Number(a.hostname ? a.port : z.location.port) || ("http" === a.protocol ? 80 : "https" === a.protocol ? 443 : "")) : "host" === b && (a.hostname = (a.hostname || z.location.hostname).replace(sf, "").toLowerCase());
      return wf(a, b, c, d, e)
  }
    , wf = function(a, b, c, d, e) {
      var f, g = vf(a.protocol);
      b && (b = String(b).toLowerCase());
      switch (b) {
      case "url_no_fragment":
          f = yf(a);
          break;
      case "protocol":
          f = g;
          break;
      case "host":
          f = a.hostname.replace(sf, "").toLowerCase();
          if (c) {
              var l = /^www\d*\./.exec(f);
              l && l[0] && (f = f.substr(l[0].length))
          }
          break;
      case "port":
          f = String(Number(a.port) || ("http" === g ? 80 : "https" === g ? 443 : ""));
          break;
      case "path":
          a.pathname || a.hostname || $a("TAGGING", 1);
          f = "/" === a.pathname.substr(0, 1) ? a.pathname : "/" + a.pathname;
          var m = f.split("/");
          0 <= (d || []).indexOf(m[m.length - 1]) && (m[m.length - 1] = "");
          f = m.join("/");
          break;
      case "query":
          f = a.search.replace("?", "");
          e && (f = uf(f, e));
          break;
      case "extension":
          var n = a.pathname.split(".");
          f = 1 < n.length ? n[n.length - 1] : "";
          f = f.split("/")[0];
          break;
      case "fragment":
          f = a.hash.replace("#", "");
          break;
      default:
          f = a && a.href
      }
      return f
  }
    , vf = function(a) {
      return a ? a.replace(":", "").toLowerCase() : ""
  }
    , yf = function(a) {
      var b = "";
      if (a && a.href) {
          var c = a.href.indexOf("#");
          b = 0 > c ? a.href : a.href.substr(0, c)
      }
      return b
  }
    , zf = function(a) {
      var b = C.createElement("a");
      a && (b.href = a);
      var c = b.pathname;
      "/" !== c[0] && (a || $a("TAGGING", 1),
      c = "/" + c);
      var d = b.hostname.replace(sf, "");
      return {
          href: b.href,
          protocol: b.protocol,
          host: b.host,
          hostname: d,
          pathname: c,
          search: b.search,
          hash: b.hash,
          port: b.port
      }
  }
    , Af = function(a) {
      function b(n) {
          var p = n.split("=")[0];
          return 0 > d.indexOf(p) ? n : p + "=0"
      }
      function c(n) {
          return n.split("&").map(b).filter(function(p) {
              return void 0 !== p
          }).join("&")
      }
      var d = "gclid dclid gbraid wbraid gclaw gcldc gclha gclgf gclgb _gl".split(" ")
        , e = zf(a)
        , f = a.split(/[?#]/)[0]
        , g = e.search
        , l = e.hash;
      "?" === g[0] && (g = g.substring(1));
      "#" === l[0] && (l = l.substring(1));
      g = c(g);
      l = c(l);
      "" !== g && (g = "?" + g);
      "" !== l && (l = "#" + l);
      var m = "" + f + g + l;
      "/" === m[m.length - 1] && (m = m.substring(0, m.length - 1));
      return m
  }
    , Bf = function(a) {
      var b = zf(z.location.href)
        , c = xf(b, "host", !1);
      if (c && c.match(tf)) {
          var d = xf(b, "path").split(a + "=");
          if (1 < d.length)
              return d[1].split(";")[0].split("?")[0]
      }
  };
  var xg = new function(a, b) {
      this.h = a;
      this.defaultValue = void 0 === b ? !1 : b
  }
  (1933);
  var yg = function(a) {
      yg[" "](a);
      return a
  };
  yg[" "] = function() {}
  ;
  var Ag = function() {
      var a = zg
        , b = "Wf";
      if (a.Wf && a.hasOwnProperty(b))
          return a.Wf;
      var c = new a;
      return a.Wf = c
  };
  var zg = function() {
      var a = {};
      this.h = function() {
          var b = xg.h
            , c = xg.defaultValue;
          return null != a[b] ? a[b] : c
      }
      ;
      this.m = function() {
          a[xg.h] = !0
      }
  };
  var Bg = !1
    , Cg = !1
    , Dg = []
    , Eg = {}
    , Fg = {}
    , Gg = {
      ad_storage: !1,
      ad_user_data: !1,
      ad_data_sharing: !1
  };
  function Hg() {
      var a = Gb("google_tag_data", {});
      a.ics || (a.ics = {
          entries: {},
          cps: {},
          default: Ig,
          update: Jg,
          declare: Kg,
          implicit: Lg,
          addListener: Mg,
          notifyListeners: Ng,
          setCps: Og,
          active: !1,
          usedDeclare: !1,
          usedDefault: !1,
          usedUpdate: !1,
          usedImplicit: !1,
          usedSetCps: !1,
          accessedDefault: !1,
          accessedAny: !1,
          wasSetLate: !1
      });
      return a.ics
  }
  function Pg(a, b, c, d) {
      return "" === c || a === d ? !0 : a === c ? b !== d : !a && !b
  }
  function Kg(a, b, c, d, e) {
      var f = Hg();
      f.active = !0;
      f.usedDeclare = !0;
      var g = f.entries
        , l = g[a] || {}
        , m = l.declare_region
        , n = c && h(c) ? c.toUpperCase() : void 0;
      d = d.toUpperCase();
      e = e.toUpperCase();
      if (Pg(n, m, d, e)) {
          var p = {
              region: l.region,
              declare_region: n,
              declare: "granted" === b,
              implicit: l.implicit,
              default: l.default,
              update: l.update,
              quiet: l.quiet
          };
          if ("" !== d || !1 !== l.declare)
              g[a] = p
      }
  }
  function Lg(a, b) {
      var c = Hg();
      c.active = !0;
      c.usedImplicit = !0;
      var d = c.entries
        , e = d[a] = d[a] || {};
      !1 !== e.implicit && (e.implicit = "granted" === b)
  }
  function Ig(a, b, c, d, e, f) {
      var g = Hg();
      g.usedDefault || !g.accessedDefault && !g.accessedAny || (g.wasSetLate = !0);
      g.active = !0;
      g.usedDefault = !0;
      $a("TAGGING", 19);
      if (void 0 == b)
          $a("TAGGING", 18);
      else {
          var l = g.entries
            , m = l[a] || {}
            , n = m.region
            , p = c && h(c) ? c.toUpperCase() : void 0;
          d = d.toUpperCase();
          e = e.toUpperCase();
          if (Pg(p, n, d, e)) {
              var q = !!(f && 0 < f && void 0 === m.update)
                , r = {
                  region: p,
                  declare_region: m.declare_region,
                  implicit: m.implicit,
                  default: "granted" === b,
                  declare: m.declare,
                  update: m.update,
                  quiet: q
              };
              if ("" !== d || !1 !== m.default)
                  l[a] = r;
              q && z.setTimeout(function() {
                  if (l[a] === r && r.quiet) {
                      r.quiet = !1;
                      var t = [a];
                      if (Ve(4))
                          for (var u in Eg)
                              Eg.hasOwnProperty(u) && Eg[u] === a && t.push(u);
                      for (var v = 0; v < t.length; v++)
                          Qg(t[v]);
                      Ng();
                      $a("TAGGING", 2)
                  }
              }, f)
          }
      }
  }
  function Jg(a, b) {
      var c = Hg();
      c.usedDefault || c.usedUpdate || !c.accessedAny || (c.wasSetLate = !0);
      c.active = !0;
      c.usedUpdate = !0;
      if (void 0 != b) {
          var d = Rg(c, a)
            , e = c.entries
            , f = e[a] = e[a] || {};
          f.update = "granted" === b;
          var g = Rg(c, a)
            , l = [a];
          if (Ve(4))
              for (var m in Eg)
                  Eg.hasOwnProperty(m) && Eg[m] === a && l.push(m);
          if (f.quiet) {
              f.quiet = !1;
              for (var n = 0; n < l.length; n++)
                  Qg(l[n])
          } else if (g !== d)
              for (var p = 0; p < l.length; p++)
                  Qg(l[p])
      }
  }
  function Og(a, b, c, d, e) {
      var f = Hg(), g;
      a: {
          var l = f.cps, m, n = l[a] || {}, p = n.region, q = c && h(c) ? c.toUpperCase() : void 0;
          m = d.toUpperCase();
          if (Pg(q, p, m, e.toUpperCase())) {
              var r = {
                  enabled: "granted" === b,
                  region: q
              };
              if ("" !== m || !1 !== n.enabled) {
                  l[a] = r;
                  g = !0;
                  break a
              }
          }
          g = !1
      }
      g && (f.usedSetCps = !0)
  }
  function Mg(a, b) {
      Dg.push({
          consentTypes: a,
          mk: b
      })
  }
  function Qg(a) {
      for (var b = 0; b < Dg.length; ++b) {
          var c = Dg[b];
          ua(c.consentTypes) && -1 !== c.consentTypes.indexOf(a) && (c.ni = !0)
      }
  }
  function Ng(a, b) {
      for (var c = 0; c < Dg.length; ++c) {
          var d = Dg[c];
          if (d.ni) {
              d.ni = !1;
              try {
                  d.mk({
                      consentEventId: a,
                      consentPriorityId: b
                  })
              } catch (e) {}
          }
      }
  }
  function Rg(a, b) {
      var c = a.entries
        , d = c[b] || {}
        , e = d.update;
      if (void 0 !== e)
          return e ? 1 : 2;
      e = d.default;
      if (void 0 !== e)
          return e ? 1 : 2;
      if (Ve(4) && Eg.hasOwnProperty(b)) {
          var f = c[Eg[b]] || {};
          e = f.update;
          if (void 0 !== e)
              return e ? 1 : 2;
          e = f.default;
          if (void 0 !== e)
              return e ? 1 : 2
      }
      e = d.declare;
      return void 0 !== e ? e ? 1 : 2 : Ve(4) && (e = d.implicit,
      void 0 !== e) ? e ? 3 : 4 : Ve(3) && Gg.hasOwnProperty(b) ? Gg[b] ? 3 : 4 : 0
  }
  var Sg = function(a) {
      var b = Hg();
      b.accessedAny = !0;
      switch (Rg(b, a)) {
      case 1:
      case 3:
          return !0;
      case 2:
      case 4:
          return !1;
      default:
          return !0
      }
  }
    , Tg = function(a) {
      var b = Hg();
      b.accessedAny = !0;
      return !(b.entries[a] || {}).quiet
  }
    , Ug = function() {
      if (!Ag().h())
          return !1;
      var a = Hg();
      a.accessedAny = !0;
      return a.active
  }
    , Vg = function() {
      var a = Hg();
      a.accessedDefault = !0;
      return a.usedDefault
  }
    , Wg = function(a, b) {
      Hg().addListener(a, b)
  }
    , Xg = function(a, b) {
      Hg().notifyListeners(a, b)
  }
    , gh = function(a, b) {
      function c() {
          for (var e = 0; e < b.length; e++)
              if (!Tg(b[e]))
                  return !0;
          return !1
      }
      if (c()) {
          var d = !1;
          Wg(b, function(e) {
              d || c() || (d = !0,
              a(e))
          })
      } else
          a({})
  }
    , hh = function(a, b) {
      function c() {
          for (var f = [], g = 0; g < d.length; g++) {
              var l = d[g];
              Sg(l) && !e[l] && (f.push(l),
              e[l] = !0)
          }
          return f
      }
      var d = h(b) ? [b] : b
        , e = {};
      c().length !== d.length && Wg(d, function(f) {
          var g = c();
          0 < g.length && (f.consentTypes = g,
          a(f))
      })
  };
  function ih() {}
  function jh() {}
  ;var kh = [N.g.D, N.g.M]
    , lh = [N.g.D, N.g.M, N.g.Vd, N.g.cf]
    , mh = {}
    , nh = (mh[N.g.D] = 1,
  mh[N.g.M] = 2,
  mh[N.g.Vd] = 3,
  mh[N.g.cf] = 4,
  mh)
    , oh = {}
    , ph = (oh[N.g.Mi] = "a",
  oh[N.g.Oi] = "s",
  oh[N.g.Pi] = "y",
  oh[N.g.Ni] = "p",
  oh)
    , qh = function(a) {
      for (var b = a[N.g.Xb], c = Array.isArray(b) ? b : [b], d = {
          Fc: 0
      }; d.Fc < c.length; d = {
          Fc: d.Fc
      },
      ++d.Fc)
          k(a, function(e) {
              return function(f, g) {
                  if (f !== N.g.Xb) {
                      var l = c[e.Fc]
                        , m = We["0"] || ""
                        , n = We["1"] || "";
                      Cg = !0;
                      Bg && $a("TAGGING", 20);
                      Hg().declare(f, g, l, m, n)
                  }
              }
          }(d))
  }
    , rh = function(a) {
      var b = a[N.g.Xb];
      b && K(40);
      var c = a[N.g.Bg];
      c && K(41);
      for (var d = ua(b) ? b : [b], e = {
          Gc: 0
      }; e.Gc < d.length; e = {
          Gc: e.Gc
      },
      ++e.Gc)
          k(a, function(f) {
              return function(g, l) {
                  if (g !== N.g.Xb && g !== N.g.Bg) {
                      var m = d[f.Gc]
                        , n = Number(c)
                        , p = We["0"] || ""
                        , q = We["1"] || "";
                      Bg = !0;
                      Cg && $a("TAGGING", 20);
                      Hg().default(g, l, m, p, q, n)
                  }
              }
          }(e))
  }
    , sh = function(a, b) {
      k(a, function(c, d) {
          Bg = !0;
          Cg && $a("TAGGING", 20);
          Hg().update(c, d)
      });
      Xg(b.eventId, b.priorityId)
  }
    , th = function(a) {
      for (var b = a[N.g.Xb], c = Array.isArray(b) ? b : [b], d = {
          Hc: 0
      }; d.Hc < c.length; d = {
          Hc: d.Hc
      },
      ++d.Hc)
          k(a, function(e) {
              return function(f, g) {
                  if (f !== N.g.Xb) {
                      var l = c[e.Hc]
                        , m = We["0"] || ""
                        , n = We["1"] || "";
                      Hg().setCps(f, g, l, m, n)
                  }
              }
          }(d))
  }
    , uh = function() {
      var a = {}, b;
      for (b in nh)
          if (nh.hasOwnProperty(b)) {
              var c = nh[b], d, e = Hg();
              e.accessedAny = !0;
              d = Rg(e, b);
              a[c] = d
          }
      if (R(104))
          return fc(a, 2);
      var f = R(111) && kh.every(Sg)
        , g = R(112);
      return f || g ? fc(a, 1) : fc(a, 0)
  }
    , vh = {}
    , wh = (vh[N.g.D] = 0,
  vh[N.g.M] = 1,
  vh[N.g.Vd] = 2,
  vh[N.g.cf] = 3,
  vh);
  function xh(a) {
      switch (a) {
      case void 0:
          return 1;
      case !0:
          return 3;
      case !1:
          return 2;
      default:
          return 0
      }
  }
  var yh = function() {
      if (R(106)) {
          for (var a = "1", b = 0; b < lh.length; b++) {
              var c = a, d, e = lh[b], f = Eg[e];
              d = void 0 === f ? 0 : wh.hasOwnProperty(f) ? 12 | wh[f] : 8;
              var g = Hg();
              g.accessedAny = !0;
              var l = g.entries[e] || {};
              d = d << 2 | xh(l.implicit);
              a = c + ("" + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"[d] + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"[xh(l.declare) << 4 | xh(l.default) << 2 | xh(l.update)])
          }
          return a
      }
      for (var m = "G1", n = 0; n < kh.length; n++) {
          var p;
          a: {
              var q = kh[n]
                , r = Hg();
              r.accessedDefault = !0;
              switch ((r.entries[q] || {}).default) {
              case !0:
                  p = 3;
                  break a;
              case !1:
                  p = 2;
                  break a;
              default:
                  p = 1
              }
          }
          switch (p) {
          case 3:
              m += "1";
              break;
          case 2:
              m += "0";
              break;
          case 1:
              m += "-"
          }
      }
      return m
  }
    , zh = function() {
      var a = Hg(), b = a.cps, c = [], d;
      for (d in Fg)
          Fg.hasOwnProperty(d) && Fg[d].enabled && (a.usedSetCps ? b.hasOwnProperty(d) && b[d].enabled && c.push(d) : c.push(d));
      for (var e = "", f = 0; f < c.length; f++) {
          var g = ph[c[f]];
          g && (e += g)
      }
      return "" === e ? "-" : e
  }
    , Ah = function() {
      return Sg(N.g.Vd) ? Ye() || Hg().usedSetCps : !1
  }
    , Bh = function(a, b) {
      hh(a, b)
  }
    , Ch = function(a, b) {
      gh(a, b)
  };
  var Dh = function(a) {
      var b = 1, c, d, e;
      if (a)
          for (b = 0,
          d = a.length - 1; 0 <= d; d--)
              e = a.charCodeAt(d),
              b = (b << 6 & 268435455) + e + (e << 14),
              c = b & 266338304,
              b = 0 !== c ? b ^ c >> 21 : b;
      return b
  };
  var Eh = function(a, b, c) {
      for (var d = [], e = b.split(";"), f = 0; f < e.length; f++) {
          var g = e[f].split("=")
            , l = g[0].replace(/^\s*|\s*$/g, "");
          if (l && l == a) {
              var m = g.slice(1).join("=").replace(/^\s*|\s*$/g, "");
              m && c && (m = decodeURIComponent(m));
              d.push(m)
          }
      }
      return d
  };
  var Fh = function(a, b) {
      var c = function() {};
      c.prototype = a.prototype;
      var d = new c;
      a.apply(d, Array.prototype.slice.call(arguments, 1));
      return d
  }
    , Gh = function(a) {
      var b = a;
      return function() {
          if (b) {
              var c = b;
              b = null;
              c()
          }
      }
  };
  function Hh(a) {
      return "null" !== a.origin
  }
  ;var Kh = function(a, b, c, d) {
      return Ih(d) ? Eh(a, String(b || Jh()), c) : []
  }
    , Nh = function(a, b, c, d, e) {
      if (Ih(e)) {
          var f = Lh(a, d, e);
          if (1 === f.length)
              return f[0].id;
          if (0 !== f.length) {
              f = Mh(f, function(g) {
                  return g.Me
              }, b);
              if (1 === f.length)
                  return f[0].id;
              f = Mh(f, function(g) {
                  return g.Hd
              }, c);
              return f[0] ? f[0].id : void 0
          }
      }
  };
  function Oh(a, b, c, d) {
      var e = Jh()
        , f = window;
      Hh(f) && (f.document.cookie = a);
      var g = Jh();
      return e != g || void 0 != c && 0 <= Kh(b, g, !1, d).indexOf(c)
  }
  var Sh = function(a, b, c) {
      function d(t, u, v) {
          if (null == v)
              return delete g[u],
              t;
          g[u] = v;
          return t + "; " + u + "=" + v
      }
      function e(t, u) {
          if (null == u)
              return delete g[u],
              t;
          g[u] = !0;
          return t + "; " + u
      }
      if (!Ih(c.kb))
          return 2;
      var f;
      void 0 == b ? f = a + "=deleted; expires=" + (new Date(0)).toUTCString() : (c.encode && (b = encodeURIComponent(b)),
      b = Ph(b),
      f = a + "=" + b);
      var g = {};
      f = d(f, "path", c.path);
      var l;
      c.expires instanceof Date ? l = c.expires.toUTCString() : null != c.expires && (l = "" + c.expires);
      f = d(f, "expires", l);
      f = d(f, "max-age", c.im);
      f = d(f, "samesite", c.jm);
      c.km && (f = e(f, "secure"));
      var m = c.domain;
      if (m && "auto" === m.toLowerCase()) {
          for (var n = Qh(), p = 0; p < n.length; ++p) {
              var q = "none" !== n[p] ? n[p] : void 0
                , r = d(f, "domain", q);
              r = e(r, c.flags);
              if (!Rh(q, c.path) && Oh(r, a, b, c.kb))
                  return 0
          }
          return 1
      }
      m && "none" !== m.toLowerCase() && (f = d(f, "domain", m));
      f = e(f, c.flags);
      return Rh(m, c.path) ? 1 : Oh(f, a, b, c.kb) ? 0 : 1
  }
    , Th = function(a, b, c) {
      null == c.path && (c.path = "/");
      c.domain || (c.domain = "auto");
      return Sh(a, b, c)
  };
  function Mh(a, b, c) {
      for (var d = [], e = [], f, g = 0; g < a.length; g++) {
          var l = a[g]
            , m = b(l);
          m === c ? d.push(l) : void 0 === f || m < f ? (e = [l],
          f = m) : m === f && e.push(l)
      }
      return 0 < d.length ? d : e
  }
  function Lh(a, b, c) {
      for (var d = [], e = Kh(a, void 0, void 0, c), f = 0; f < e.length; f++) {
          var g = e[f].split(".")
            , l = g.shift();
          if (!b || -1 !== b.indexOf(l)) {
              var m = g.shift();
              m && (m = m.split("-"),
              d.push({
                  id: g.join("."),
                  Me: 1 * m[0] || 1,
                  Hd: 1 * m[1] || 1
              }))
          }
      }
      return d
  }
  var Ph = function(a) {
      a && 1200 < a.length && (a = a.substring(0, 1200));
      return a
  }
    , Uh = /^(www\.)?google(\.com?)?(\.[a-z]{2})?$/
    , Vh = /(^|\.)doubleclick\.net$/i
    , Rh = function(a, b) {
      return Vh.test(window.document.location.hostname) || "/" === b && Uh.test(a)
  }
    , Jh = function() {
      return Hh(window) ? window.document.cookie : ""
  }
    , Qh = function() {
      var a = []
        , b = window.document.location.hostname.split(".");
      if (4 === b.length) {
          var c = b[b.length - 1];
          if (parseInt(c, 10).toString() === c)
              return ["none"]
      }
      for (var d = b.length - 2; 0 <= d; d--)
          a.push(b.slice(d).join("."));
      var e = window.document.location.hostname;
      Vh.test(e) || Uh.test(e) || a.push("none");
      return a
  }
    , Ih = function(a) {
      return Ag().h() && a && Ug() ? Tg(a) ? Sg(a) : !1 : !0
  };
  var Wh = function(a) {
      var b = Math.round(2147483647 * Math.random());
      return a ? String(b ^ Dh(a) & 2147483647) : String(b)
  }
    , Xh = function(a) {
      return [Wh(a), Math.round(Ha() / 1E3)].join(".")
  }
    , $h = function(a, b, c, d, e) {
      var f = Yh(b);
      return Nh(a, f, Zh(c), d, e)
  }
    , ai = function(a, b, c, d) {
      var e = "" + Yh(c)
        , f = Zh(d);
      1 < f && (e += "-" + f);
      return [b, e, a].join(".")
  }
    , Yh = function(a) {
      if (!a)
          return 1;
      a = 0 === a.indexOf(".") ? a.substr(1) : a;
      return a.split(".").length
  }
    , Zh = function(a) {
      if (!a || "/" === a)
          return 1;
      "/" !== a[0] && (a = "/" + a);
      "/" !== a[a.length - 1] && (a += "/");
      return a.split("/").length - 1
  };
  var bi = function() {
      oe.dedupe_gclid || (oe.dedupe_gclid = "" + Xh());
      return oe.dedupe_gclid
  };
  var ci = function() {
      var a = !1;
      return a
  };
  var ei = function(a) {
      var b = di();
      b.pending || (b.pending = []);
      va(b.pending, function(c) {
          return c.target.ctid === a.ctid && c.target.isDestination === a.isDestination
      }) || b.pending.push({
          target: a,
          onLoad: void 0
      })
  }
    , fi = function() {
      this.container = {};
      this.destination = {};
      this.canonical = {};
      this.pending = []
  }
    , di = function() {
      var a = Gb("google_tag_data", {})
        , b = a.tidr;
      b || (b = new fi,
      a.tidr = b);
      return b
  };
  var T = {
      C: "GTM-PNVLDT6",
      Ua: "9560941"
  }
    , gi = {
      li: "GTM-PNVLDT6",
      mi: "GTM-PNVLDT6"
  };
  T.Ce = Da("");
  var hi = function() {
      return gi.li ? gi.li.split("|") : [T.C]
  }
    , ii = function() {
      return gi.mi ? gi.mi.split("|") : []
  }
    , ji = function(a) {
      var b = di();
      return a.isDestination ? b.destination[a.ctid] : b.container[a.ctid]
  };
  function ki() {
      var a = di();
      if (a.pending) {
          for (var b, c = [], d = !1, e = hi(), f = ii(), g = {}, l = 0; l < a.pending.length; g = {
              Vb: g.Vb
          },
          l++)
              g.Vb = a.pending[l],
              va(g.Vb.target.isDestination ? f : e, function(m) {
                  return function(n) {
                      return n === m.Vb.target.ctid
                  }
              }(g)) ? d || (b = g.Vb.onLoad,
              d = !0) : c.push(g.Vb);
          a.pending = c;
          if (b)
              try {
                  b(T.Ua || "_" + T.C)
              } catch (m) {}
      }
  }
  var li = function() {
      for (var a = di(), b = hi(), c = 0; c < b.length; c++) {
          var d = a.container[b[c]];
          d ? (d.state = 2,
          d.containers = hi(),
          d.destinations = ii()) : a.container[b[c]] = {
              state: 2,
              containers: hi(),
              destinations: ii()
          }
      }
      for (var e = ii(), f = 0; f < e.length; f++) {
          var g = a.destination[e[f]];
          g && 0 === g.state && K(93);
          g ? (g.state = 2,
          g.containers = hi(),
          g.destinations = ii()) : a.destination[e[f]] = {
              state: 2,
              containers: hi(),
              destinations: ii()
          }
      }
      ki()
  }
    , mi = function(a) {
      return !!di().container[a]
  }
    , ni = function() {
      return {
          ctid: T.C,
          isDestination: T.Ce
      }
  }
    , oi = function() {
      var a = di().container, b;
      for (b in a)
          if (a.hasOwnProperty(b) && 1 === a[b].state)
              return !0;
      return !1
  }
    , pi = function() {
      var a = {};
      k(di().destination, function(b, c) {
          0 === c.state && (a[b] = c)
      });
      return a
  };
  var qi = {
      UA: 1,
      AW: 2,
      DC: 3,
      G: 4,
      GF: 5,
      GT: 12,
      GTM: 14,
      HA: 6,
      MC: 7
  }
    , ri = function(a) {
      var b = T.C.split("-")[0].toUpperCase()
        , c = {};
      c.ctid = T.C;
      c.vl = ne.rd;
      c.yl = ne.Kf;
      c.Sk = T.Ce ? 2 : 1;
      ve ? (c.We = qi[b],
      c.We || (c.We = 0)) : c.We = Be ? 13 : 10;
      ze ? c.ig = 1 : ci() ? c.ig = 2 : c.ig = 3;
      var d;
      var e = c.We
        , f = c.ig;
      void 0 === e ? d = "" : (f || (f = 0),
      d = "" + vd(1, 1) + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"[e << 2 | f]);
      var g = c.am, l = 4 + d + (g ? "" + vd(2, 1) + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"[g] : ""), m, n = c.yl;
      m = n && ud.test(n) ? "" + vd(3, 2) + n : "";
      var p, q = c.vl;
      p = q ? "" + vd(4, 1) + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"[q] : "";
      var r;
      var t = c.ctid;
      if (t && a) {
          var u = t.split("-")
            , v = u[0].toUpperCase();
          if ("GTM" !== v && "OPT" !== v)
              r = "";
          else {
              var w = u[1];
              r = "" + vd(5, 3) + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"[1 + w.length] + (c.Sk || 0) + w
          }
      } else
          r = "";
      return l + m + p + r
  };
  function si(a, b) {
      if ("" === a)
          return b;
      var c = Number(a);
      return isNaN(c) ? b : c
  }
  ;var ti = function(a, b, c) {
      a.addEventListener && a.addEventListener(b, c, !1)
  };
  function ui() {
      return ib ? !!pb && !!pb.platform : !1
  }
  function vi() {
      return sb("iPhone") && !sb("iPod") && !sb("iPad")
  }
  function wi() {
      vi() || sb("iPad") || sb("iPod")
  }
  ;ub();
  tb() || sb("Trident") || sb("MSIE");
  sb("Edge");
  !sb("Gecko") || -1 != ob().toLowerCase().indexOf("webkit") && !sb("Edge") || sb("Trident") || sb("MSIE") || sb("Edge");
  -1 != ob().toLowerCase().indexOf("webkit") && !sb("Edge") && sb("Mobile");
  ui() || sb("Macintosh");
  ui() || sb("Windows");
  (ui() ? "Linux" === pb.platform : sb("Linux")) || ui() || sb("CrOS");
  var xi = pa.navigator || null;
  xi && (xi.appVersion || "").indexOf("X11");
  ui() || sb("Android");
  vi();
  sb("iPad");
  sb("iPod");
  wi();
  ob().toLowerCase().indexOf("kaios");
  var yi = function(a, b, c, d) {
      for (var e = b, f = c.length; 0 <= (e = a.indexOf(c, e)) && e < d; ) {
          var g = a.charCodeAt(e - 1);
          if (38 == g || 63 == g) {
              var l = a.charCodeAt(e + f);
              if (!l || 61 == l || 38 == l || 35 == l)
                  return e
          }
          e += f + 1
      }
      return -1
  }
    , zi = /#|$/
    , Ai = function(a, b) {
      var c = a.search(zi)
        , d = yi(a, 0, b, c);
      if (0 > d)
          return null;
      var e = a.indexOf("&", d);
      if (0 > e || e > c)
          e = c;
      d += b.length + 1;
      return decodeURIComponent(a.slice(d, -1 !== e ? e : 0).replace(/\+/g, " "))
  }
    , Bi = /[?&]($|#)/
    , Ci = function(a, b, c) {
      for (var d, e = a.search(zi), f = 0, g, l = []; 0 <= (g = yi(a, f, b, e)); )
          l.push(a.substring(f, g)),
          f = Math.min(a.indexOf("&", g) + 1 || e, e);
      l.push(a.slice(f));
      d = l.join("").replace(Bi, "$1");
      var m, n = null != c ? "=" + encodeURIComponent(String(c)) : "";
      var p = b + n;
      if (p) {
          var q, r = d.indexOf("#");
          0 > r && (r = d.length);
          var t = d.indexOf("?"), u;
          0 > t || t > r ? (t = r,
          u = "") : u = d.substring(t + 1, r);
          q = [d.slice(0, t), u, d.slice(r)];
          var v = q[1];
          q[1] = p ? v ? v + "&" + p : p : v;
          m = q[0] + (q[1] ? "?" + q[1] : "") + q[2]
      } else
          m = d;
      return m
  };
  var Di = function(a) {
      try {
          var b;
          if (b = !!a && null != a.location.href)
              a: {
                  try {
                      yg(a.foo);
                      b = !0;
                      break a
                  } catch (c) {}
                  b = !1
              }
          return b
      } catch (c) {
          return !1
      }
  }
    , Ei = function(a, b) {
      if (a)
          for (var c in a)
              Object.prototype.hasOwnProperty.call(a, c) && b(a[c], c, a)
  };
  function Fi(a) {
      if (!a || !C.head)
          return null;
      var b = Gi("META");
      C.head.appendChild(b);
      b.httpEquiv = "origin-trial";
      b.content = a;
      return b
  }
  var Hi = function() {
      if (z.top == z)
          return 0;
      var a = z.location.ancestorOrigins;
      return a ? a[a.length - 1] == z.location.origin ? 1 : 2 : Di(z.top) ? 1 : 2
  }
    , Gi = function(a, b) {
      b = void 0 === b ? document : b;
      return b.createElement(String(a).toLowerCase())
  };
  function Ii(a, b, c, d) {
      d = void 0 === d ? !1 : d;
      a.google_image_requests || (a.google_image_requests = []);
      var e = Gi("IMG", a.document);
      if (c) {
          var f = function() {
              if (c) {
                  var g = a.google_image_requests
                    , l = cb(g, e);
                  0 <= l && Array.prototype.splice.call(g, l, 1)
              }
              e.removeEventListener && e.removeEventListener("load", f, !1);
              e.removeEventListener && e.removeEventListener("error", f, !1)
          };
          ti(e, "load", f);
          ti(e, "error", f)
      }
      d && (e.attributionSrc = "");
      e.src = b;
      a.google_image_requests.push(e)
  }
  var Ki = function(a) {
      var b;
      b = void 0 === b ? !1 : b;
      var c = "https://pagead2.googlesyndication.com/pagead/gen_204?id=tcfe";
      Ei(a, function(d, e) {
          if (d || 0 === d)
              c += "&" + e + "=" + encodeURIComponent("" + d)
      });
      Ji(c, b)
  }
    , Ji = function(a, b) {
      var c = window, d;
      b = void 0 === b ? !1 : b;
      d = void 0 === d ? !1 : d;
      if (c.fetch) {
          var e = {
              keepalive: !0,
              credentials: "include",
              redirect: "follow",
              method: "get",
              mode: "no-cors"
          };
          d && (e.mode = "cors",
          "setAttributionReporting"in XMLHttpRequest.prototype ? e.attributionReporting = {
              eventSourceEligible: "true",
              triggerEligible: "false"
          } : e.headers = {
              "Attribution-Reporting-Eligible": "event-source"
          });
          c.fetch(a, e)
      } else
          Ii(c, a, void 0 === b ? !1 : b, void 0 === d ? !1 : d)
  };
  var Li = function() {};
  var Mi = function(a) {
      void 0 !== a.addtlConsent && "string" !== typeof a.addtlConsent && (a.addtlConsent = void 0);
      void 0 !== a.gdprApplies && "boolean" !== typeof a.gdprApplies && (a.gdprApplies = void 0);
      return void 0 !== a.tcString && "string" !== typeof a.tcString || void 0 !== a.listenerId && "number" !== typeof a.listenerId ? 2 : a.cmpStatus && "error" !== a.cmpStatus ? 0 : 3
  }
    , Ni = function(a, b) {
      b = void 0 === b ? {} : b;
      this.m = a;
      this.h = null;
      this.J = {};
      this.Bb = 0;
      var c;
      this.X = null != (c = b.Fl) ? c : 500;
      var d;
      this.H = null != (d = b.bm) ? d : !1;
      this.B = null
  };
  oa(Ni, Li);
  Ni.prototype.addEventListener = function(a) {
      var b = this
        , c = {
          internalBlockOnErrors: this.H
      }
        , d = Gh(function() {
          return a(c)
      })
        , e = 0;
      -1 !== this.X && (e = setTimeout(function() {
          c.tcString = "tcunavailable";
          c.internalErrorState = 1;
          d()
      }, this.X));
      var f = function(g, l) {
          clearTimeout(e);
          g ? (c = g,
          c.internalErrorState = Mi(c),
          c.internalBlockOnErrors = b.H,
          l && 0 === c.internalErrorState || (c.tcString = "tcunavailable",
          l || (c.internalErrorState = 3))) : (c.tcString = "tcunavailable",
          c.internalErrorState = 3);
          a(c)
      };
      try {
          Oi(this, "addEventListener", f)
      } catch (g) {
          c.tcString = "tcunavailable",
          c.internalErrorState = 3,
          e && (clearTimeout(e),
          e = 0),
          d()
      }
  }
  ;
  Ni.prototype.removeEventListener = function(a) {
      a && a.listenerId && Oi(this, "removeEventListener", null, a.listenerId)
  }
  ;
  var Qi = function(a, b, c) {
      var d;
      d = void 0 === d ? "755" : d;
      var e;
      a: {
          if (a.publisher && a.publisher.restrictions) {
              var f = a.publisher.restrictions[b];
              if (void 0 !== f) {
                  e = f[void 0 === d ? "755" : d];
                  break a
              }
          }
          e = void 0
      }
      var g = e;
      if (0 === g)
          return !1;
      var l = c;
      2 === c ? (l = 0,
      2 === g && (l = 1)) : 3 === c && (l = 1,
      1 === g && (l = 0));
      var m;
      if (0 === l)
          if (a.purpose && a.vendor) {
              var n = Pi(a.vendor.consents, void 0 === d ? "755" : d);
              m = n && "1" === b && a.purposeOneTreatment && "CH" === a.publisherCC ? !0 : n && Pi(a.purpose.consents, b)
          } else
              m = !0;
      else
          m = 1 === l ? a.purpose && a.vendor ? Pi(a.purpose.legitimateInterests, b) && Pi(a.vendor.legitimateInterests, void 0 === d ? "755" : d) : !0 : !0;
      return m
  }
    , Pi = function(a, b) {
      return !(!a || !a[b])
  }
    , Oi = function(a, b, c, d) {
      c || (c = function() {}
      );
      if ("function" === typeof a.m.__tcfapi) {
          var e = a.m.__tcfapi;
          e(b, 2, c, d)
      } else if (Ri(a)) {
          Si(a);
          var f = ++a.Bb;
          a.J[f] = c;
          if (a.h) {
              var g = {};
              a.h.postMessage((g.__tcfapiCall = {
                  command: b,
                  version: 2,
                  callId: f,
                  parameter: d
              },
              g), "*")
          }
      } else
          c({}, !1)
  }
    , Ri = function(a) {
      if (a.h)
          return a.h;
      var b;
      a: {
          for (var c = a.m, d = 0; 50 > d; ++d) {
              var e;
              try {
                  e = !(!c.frames || !c.frames.__tcfapiLocator)
              } catch (l) {
                  e = !1
              }
              if (e) {
                  b = c;
                  break a
              }
              var f;
              b: {
                  try {
                      var g = c.parent;
                      if (g && g != c) {
                          f = g;
                          break b
                      }
                  } catch (l) {}
                  f = null
              }
              if (!(c = f))
                  break
          }
          b = null
      }
      a.h = b;
      return a.h
  }
    , Si = function(a) {
      a.B || (a.B = function(b) {
          try {
              var c;
              c = ("string" === typeof b.data ? JSON.parse(b.data) : b.data).__tcfapiReturn;
              a.J[c.callId](c.returnValue, c.success)
          } catch (d) {}
      }
      ,
      ti(a.m, "message", a.B))
  }
    , Ti = function(a) {
      if (!1 === a.gdprApplies)
          return !0;
      void 0 === a.internalErrorState && (a.internalErrorState = Mi(a));
      return "error" === a.cmpStatus || 0 !== a.internalErrorState ? a.internalBlockOnErrors ? (Ki({
          e: String(a.internalErrorState)
      }),
      !1) : !0 : "loaded" !== a.cmpStatus || "tcloaded" !== a.eventStatus && "useractioncomplete" !== a.eventStatus ? !1 : !0
  };
  var Ui = {
      1: 0,
      3: 0,
      4: 0,
      7: 3,
      9: 3,
      10: 3
  }
    , Vi = si('', 500);
  function Wi() {
      var a = oe.tcf || {};
      return oe.tcf = a
  }
  var bj = function() {
      var a = Wi()
        , b = new Ni(z,{
          Fl: -1
      });
      Xi(b) && Yi() && K(124);
      if (!Yi() && !a.active && Xi(b)) {
          a.active = !0;
          a.Te = {};
          Zi();
          a.tcString = "tcunavailable";
          try {
              b.addEventListener(function(c) {
                  if (0 !== c.internalErrorState)
                      $i(a),
                      aj(a);
                  else {
                      var d;
                      a.gdprApplies = c.gdprApplies;
                      if (!1 === c.gdprApplies) {
                          var e = {}, f;
                          for (f in Ui)
                              Ui.hasOwnProperty(f) && (e[f] = !0);
                          d = e;
                          b.removeEventListener(c)
                      } else if ("tcloaded" === c.eventStatus || "useractioncomplete" === c.eventStatus || "cmpuishown" === c.eventStatus) {
                          var g = {}, l;
                          for (l in Ui)
                              if (Ui.hasOwnProperty(l))
                                  if ("1" === l) {
                                      var m, n = c, p = !0;
                                      p = void 0 === p ? !1 : p;
                                      m = Ti(n) ? !1 === n.gdprApplies || "tcunavailable" === n.tcString || void 0 === n.gdprApplies && !p || "string" !== typeof n.tcString || !n.tcString.length ? !0 : Qi(n, "1", 0) : !1;
                                      g["1"] = m
                                  } else
                                      g[l] = Qi(c, l, Ui[l]);
                          d = g
                      }
                      d && (a.tcString = c.tcString || "tcempty",
                      a.Te = d,
                      aj(a))
                  }
              })
          } catch (c) {
              $i(a),
              aj(a)
          }
      }
  };
  function $i(a) {
      a.type = "e";
      a.tcString = "tcunavailable"
  }
  function Zi() {
      var a = {}
        , b = (a.ad_storage = "denied",
      a.wait_for_update = Vi,
      a);
      rh(b)
  }
  function Xi(a) {
      return "function" === typeof z.__tcfapi || "function" === typeof a.m.__tcfapi || null != Ri(a) ? !0 : !1
  }
  var Yi = function() {
      return !0 !== z.gtag_enable_tcf_support
  };
  function aj(a) {
      var b = {}
        , c = (b.ad_storage = a.Te["1"] ? "granted" : "denied",
      b);
      sh(c, {
          eventId: 0
      }, {
          gdprApplies: a ? a.gdprApplies : void 0,
          tcString: cj()
      })
  }
  var cj = function() {
      var a = Wi();
      return a.active ? a.tcString || "" : ""
  }
    , dj = function() {
      var a = Wi();
      return a.active && void 0 !== a.gdprApplies ? a.gdprApplies ? "1" : "0" : ""
  }
    , ej = function(a) {
      if (!Ui.hasOwnProperty(String(a)))
          return !0;
      var b = Wi();
      return b.active && b.Te ? !!b.Te[String(a)] : !0
  };
  var fj = function(a) {
      var b = String(a[gc.zb] || "").replace(/_/g, "");
      0 === b.indexOf("cvt") && (b = "cvt");
      return b
  }
    , gj = 0 <= z.location.search.indexOf("?gtm_latency=") || 0 <= z.location.search.indexOf("&gtm_latency=");
  var hj = {
      sampleRate: "0.005000",
      Fi: "",
      Ei: Number("5"),
      mm: Number("")
  }, ij = [], jj;
  if (!(jj = gj)) {
      var kj = Math.random()
        , lj = hj.sampleRate;
      jj = kj < lj
  }
  var mj = jj
    , nj = "https://www.googletagmanager.com/a?id=" + T.C + "&cv=13";
  function oj() {
      return [nj, "&v=3&t=t", "&pid=" + wa(), "&rv=" + ne.Kf].join("")
  }
  var pj = oj();
  function qj() {
      pj = oj()
  }
  var rj = {}
    , sj = ""
    , tj = ""
    , uj = ""
    , vj = ""
    , wj = []
    , xj = ""
    , yj = void 0
    , zj = {}
    , Aj = {}
    , Bj = void 0
    , Cj = 5;
  0 < hj.Ei && (Cj = hj.Ei);
  var Dj = function(a, b) {
      for (var c = 0, d = [], e = 0; e < a; ++e)
          d.push(0);
      return {
          Jk: function() {
              return c < a ? !1 : Ha() - d[c % a] < b
          },
          pl: function() {
              var f = c++ % a;
              d[f] = Ha()
          }
      }
  }(Cj, 1E3)
    , Ej = 1E3;
  function Fj(a) {
      var b = yj;
      if (void 0 === b)
          return "";
      for (var c = [pj, rj[b] ? "" : "&es=1", zj[b], Gj(), sj, tj, uj, vj, xj ? "&dl=" + encodeURIComponent(xj) : "", 0 < wj.length ? "&tdp=" + wj.join(".") : "", ne.rd ? "&x=" + ne.rd : ""], d = 0; d < ij.length; d++) {
          var e = ij[d]({
              eventId: b,
              zg: !!a
          });
          "&" === e[0] && c.push(e)
      }
      c.push("&z=0");
      return c.join("")
  }
  function Hj() {
      Bj && (z.clearTimeout(Bj),
      Bj = void 0);
      if (void 0 !== yj)
          if (!rj[yj] || sj || tj)
              if (Aj[yj] || Dj.Jk() || 0 >= Ej--)
                  K(1),
                  Aj[yj] = !0;
              else {
                  Dj.pl();
                  var a = Fj(!0);
                  Ob(a);
                  if (vj || xj && 0 < wj.length) {
                      var b = a.replace("/a?", "/td?");
                      Ob(b)
                  }
                  rj[yj] = !0;
                  xj = vj = uj = tj = sj = "";
                  wj = []
              }
          else
              K(133)
  }
  function Ij() {
      Bj || (Bj = z.setTimeout(Hj, 500))
  }
  function Gj() {
      return "&tc=" + Hc.filter(function(a) {
          return a
      }).length
  }
  var Jj = function(a, b) {
      if (mj && !Aj[a] && yj !== a) {
          Hj();
          yj = a;
          uj = sj = "";
          var c;
          c = b.match(/^(gtm|gtag)\./) ? encodeURIComponent(b) : "*";
          zj[a] = "&e=" + c + "&eid=" + a;
          Ij()
      }
  }
    , Kj = function(a, b, c) {
      if (mj && b) {
          var d = fj(b)
            , e = c + d;
          if (!Aj[a]) {
              a !== yj && (Hj(),
              yj = a);
              sj = sj ? sj + "." + e : "&tr=" + e;
              var f = b["function"];
              if (!f)
                  throw Error("Error: No function name given for function call.");
              var g = (Jc[f] ? "1" : "2") + d;
              uj = uj ? uj + "." + g : "&ti=" + g;
              Ij();
              2022 <= Fj().length && Hj()
          }
      }
  }
    , Lj = function(a, b, c) {
      if (mj && void 0 !== a && !Aj[a]) {
          a !== yj && (Hj(),
          yj = a);
          var d = c + b;
          tj = tj ? tj + "." + d : "&epr=" + d;
          Ij();
          2022 <= Fj().length && Hj()
      }
  };
  var Mj = void 0;
  function Nj(a) {
      var b = "";
      return b
  }
  ;vb();
  vi() || sb("iPod");
  sb("iPad");
  !sb("Android") || wb() || vb() || ub() || sb("Silk");
  wb();
  !sb("Safari") || wb() || (tb() ? 0 : sb("Coast")) || ub() || (tb() ? 0 : sb("Edge")) || (tb() ? rb("Microsoft Edge") : sb("Edg/")) || (tb() ? rb("Opera") : sb("OPR")) || vb() || sb("Silk") || sb("Android") || wi();
  var Oj = {}
    , Pj = null
    , Qj = function(a) {
      for (var b = [], c = 0, d = 0; d < a.length; d++) {
          var e = a.charCodeAt(d);
          255 < e && (b[c++] = e & 255,
          e >>= 8);
          b[c++] = e
      }
      var f = 4;
      void 0 === f && (f = 0);
      if (!Pj) {
          Pj = {};
          for (var g = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""), l = ["+/=", "+/", "-_=", "-_.", "-_"], m = 0; 5 > m; m++) {
              var n = g.concat(l[m].split(""));
              Oj[m] = n;
              for (var p = 0; p < n.length; p++) {
                  var q = n[p];
                  void 0 === Pj[q] && (Pj[q] = p)
              }
          }
      }
      for (var r = Oj[f], t = Array(Math.floor(b.length / 3)), u = r[64] || "", v = 0, w = 0; v < b.length - 2; v += 3) {
          var x = b[v]
            , y = b[v + 1]
            , A = b[v + 2]
            , B = r[x >> 2]
            , D = r[(x & 3) << 4 | y >> 4]
            , I = r[(y & 15) << 2 | A >> 6]
            , H = r[A & 63];
          t[w++] = "" + B + D + I + H
      }
      var E = 0
        , L = u;
      switch (b.length - v) {
      case 2:
          E = b[v + 1],
          L = r[(E & 15) << 2] || u;
      case 1:
          var M = b[v];
          t[w] = "" + r[M >> 2] + r[(M & 3) << 4 | E >> 4] + L + u
      }
      return t.join("")
  };
  var Rj = "platform platformVersion architecture model uaFullVersion bitness fullVersionList wow64".split(" ");
  function Sj() {
      var a;
      return null != (a = z.google_tag_data) ? a : z.google_tag_data = {}
  }
  function Tj() {
      var a = z.google_tag_data, b;
      if (null != a && a.uach) {
          var c = a.uach
            , d = Object.assign({}, c);
          c.fullVersionList && (d.fullVersionList = c.fullVersionList.slice(0));
          b = d
      } else
          b = null;
      return b
  }
  function Uj() {
      var a, b;
      return null != (b = null == (a = z.google_tag_data) ? void 0 : a.uach_promise) ? b : null
  }
  function Vj() {
      var a, b;
      return "function" === typeof (null == (a = z.navigator) ? void 0 : null == (b = a.userAgentData) ? void 0 : b.getHighEntropyValues)
  }
  function Wj() {
      if (!Vj())
          return null;
      var a = Sj();
      if (a.uach_promise)
          return a.uach_promise;
      var b = z.navigator.userAgentData.getHighEntropyValues(Rj).then(function(c) {
          null != a.uach || (a.uach = c);
          return c
      });
      return a.uach_promise = b
  }
  ;var Xj, Yj = function() {
      if (Vj() && (Xj = Ha(),
      !Uj())) {
          var a = Wj();
          a && (a.then(function() {
              K(95);
          }),
          a.catch(function() {
              K(96)
          }))
      }
  }, ak = function(a) {
      var b = Zj.Jl
        , c = function(g, l) {
          try {
              a(g, l)
          } catch (m) {}
      }
        , d = Tj();
      if (d)
          c(d);
      else {
          var e = Uj();
          if (e) {
              b = Math.min(Math.max(isFinite(b) ? b : 0, 0), 1E3);
              var f = z.setTimeout(function() {
                  c.Ed || (c.Ed = !0,
                  K(106),
                  c(null, Error("Timeout")))
              }, b);
              e.then(function(g) {
                  c.Ed || (c.Ed = !0,
                  K(104),
                  z.clearTimeout(f),
                  c(g))
              }).catch(function(g) {
                  c.Ed || (c.Ed = !0,
                  K(105),
                  z.clearTimeout(f),
                  c(null, g))
              })
          } else
              c(null)
      }
  }, sk = function(a, b) {
      a && (b.m[N.g.ed] = a.architecture,
      b.m[N.g.fd] = a.bitness,
      a.fullVersionList && (b.m[N.g.gd] = a.fullVersionList.map(function(c) {
          return encodeURIComponent(c.brand || "") + ";" + encodeURIComponent(c.version || "")
      }).join("|")),
      b.m[N.g.hd] = a.mobile ? "1" : "0",
      b.m[N.g.jd] = a.model,
      b.m[N.g.kd] = a.platform,
      b.m[N.g.ld] = a.platformVersion,
      b.m[N.g.md] = a.wow64 ? "1" : "0")
  };
  function tk(a, b, c, d) {
      var e, f = Number(null != a.ib ? a.ib : void 0);
      0 !== f && (e = new Date((b || Ha()) + 1E3 * (f || 7776E3)));
      return {
          path: a.path,
          domain: a.domain,
          flags: a.flags,
          encode: !!c,
          expires: e,
          kb: d
      }
  }
  ;var uk;
  var yk = function() {
      var a = vk
        , b = wk
        , c = xk()
        , d = function(g) {
          a(g.target || g.srcElement || {})
      }
        , e = function(g) {
          b(g.target || g.srcElement || {})
      };
      if (!c.init) {
          Pb(C, "mousedown", d);
          Pb(C, "keyup", d);
          Pb(C, "submit", e);
          var f = HTMLFormElement.prototype.submit;
          HTMLFormElement.prototype.submit = function() {
              b(this);
              f.call(this)
          }
          ;
          c.init = !0
      }
  }
    , zk = function(a, b, c, d, e) {
      var f = {
          callback: a,
          domains: b,
          fragment: 2 === c,
          placement: c,
          forms: d,
          sameHost: e
      };
      xk().decorators.push(f)
  }
    , Ak = function(a, b, c) {
      for (var d = xk().decorators, e = {}, f = 0; f < d.length; ++f) {
          var g = d[f], l;
          if (l = !c || g.forms)
              a: {
                  var m = g.domains
                    , n = a
                    , p = !!g.sameHost;
                  if (m && (p || n !== C.location.hostname))
                      for (var q = 0; q < m.length; q++)
                          if (m[q]instanceof RegExp) {
                              if (m[q].test(n)) {
                                  l = !0;
                                  break a
                              }
                          } else if (0 <= n.indexOf(m[q]) || p && 0 <= m[q].indexOf(n)) {
                              l = !0;
                              break a
                          }
                  l = !1
              }
          if (l) {
              var r = g.placement;
              void 0 == r && (r = g.fragment ? 2 : 1);
              r === b && Ka(e, g.callback())
          }
      }
      return e
  };
  function xk() {
      var a = Gb("google_tag_data", {})
        , b = a.gl;
      b && b.decorators || (b = {
          decorators: []
      },
      a.gl = b);
      return b
  }
  ;var Bk = /(.*?)\*(.*?)\*(.*)/
    , Ck = /^https?:\/\/([^\/]*?)\.?cdn\.ampproject\.org\/?(.*)/
    , Dk = /^(?:www\.|m\.|amp\.)+/
    , Ek = /([^?#]+)(\?[^#]*)?(#.*)?/;
  function Fk(a) {
      return new RegExp("(.*?)(^|&)" + a + "=([^&]*)&?(.*)")
  }
  var Hk = function(a) {
      var b = [], c;
      for (c in a)
          if (a.hasOwnProperty(c)) {
              var d = a[c];
              void 0 !== d && d === d && null !== d && "[object Object]" !== d.toString() && (b.push(c),
              b.push(Wa(String(d))))
          }
      var e = b.join("*");
      return ["1", Gk(e), e].join("*")
  };
  function Gk(a, b) {
      var c = [Db.userAgent, (new Date).getTimezoneOffset(), Db.userLanguage || Db.language, Math.floor(Ha() / 60 / 1E3) - (void 0 === b ? 0 : b), a].join("*"), d;
      if (!(d = uk)) {
          for (var e = Array(256), f = 0; 256 > f; f++) {
              for (var g = f, l = 0; 8 > l; l++)
                  g = g & 1 ? g >>> 1 ^ 3988292384 : g >>> 1;
              e[f] = g
          }
          d = e
      }
      uk = d;
      for (var m = 4294967295, n = 0; n < c.length; n++)
          m = m >>> 8 ^ uk[(m ^ c.charCodeAt(n)) & 255];
      return ((m ^ -1) >>> 0).toString(36)
  }
  function Ik() {
      return function(a) {
          var b = zf(z.location.href)
            , c = b.search.replace("?", "")
            , d = uf(c, "_gl", !0) || "";
          a.query = Jk(d) || {};
          var e = xf(b, "fragment").match(Fk("_gl"));
          a.fragment = Jk(e && e[3] || "") || {}
      }
  }
  function Kk(a, b) {
      var c = Fk(a).exec(b)
        , d = b;
      if (c) {
          var e = c[2]
            , f = c[4];
          d = c[1];
          f && (d = d + e + f)
      }
      return d
  }
  var Lk = function(a, b) {
      b || (b = "_gl");
      var c = Ek.exec(a);
      if (!c)
          return "";
      var d = c[1]
        , e = Kk(b, (c[2] || "").slice(1))
        , f = Kk(b, (c[3] || "").slice(1));
      e.length && (e = "?" + e);
      f.length && (f = "#" + f);
      return "" + d + e + f
  }
    , Mk = function(a) {
      var b = Ik()
        , c = xk();
      c.data || (c.data = {
          query: {},
          fragment: {}
      },
      b(c.data));
      var d = {}
        , e = c.data;
      e && (Ka(d, e.query),
      a && Ka(d, e.fragment));
      return d
  }
    , Jk = function(a) {
      try {
          var b = Nk(a, 3);
          if (void 0 !== b) {
              for (var c = {}, d = b ? b.split("*") : [], e = 0; e + 1 < d.length; e += 2) {
                  var f = d[e]
                    , g = Xa(d[e + 1]);
                  c[f] = g
              }
              $a("TAGGING", 6);
              return c
          }
      } catch (l) {
          $a("TAGGING", 8)
      }
  };
  function Nk(a, b) {
      if (a) {
          var c;
          a: {
              for (var d = a, e = 0; 3 > e; ++e) {
                  var f = Bk.exec(d);
                  if (f) {
                      c = f;
                      break a
                  }
                  d = decodeURIComponent(d)
              }
              c = void 0
          }
          var g = c;
          if (g && "1" === g[1]) {
              var l = g[3], m;
              a: {
                  for (var n = g[2], p = 0; p < b; ++p)
                      if (n === Gk(l, p)) {
                          m = !0;
                          break a
                      }
                  m = !1
              }
              if (m)
                  return l;
              $a("TAGGING", 7)
          }
      }
  }
  function Ok(a, b, c, d) {
      function e(p) {
          p = Kk(a, p);
          var q = p.charAt(p.length - 1);
          p && "&" !== q && (p += "&");
          return p + n
      }
      d = void 0 === d ? !1 : d;
      var f = Ek.exec(c);
      if (!f)
          return "";
      var g = f[1]
        , l = f[2] || ""
        , m = f[3] || ""
        , n = a + "=" + b;
      d ? m = "#" + e(m.substring(1)) : l = "?" + e(l.substring(1));
      return "" + g + l + m
  }
  function Pk(a, b) {
      var c = "FORM" === (a.tagName || "").toUpperCase()
        , d = Ak(b, 1, c)
        , e = Ak(b, 2, c)
        , f = Ak(b, 3, c);
      if (La(d)) {
          var g = Hk(d);
          c ? Qk("_gl", g, a) : Rk("_gl", g, a, !1)
      }
      if (!c && La(e)) {
          var l = Hk(e);
          Rk("_gl", l, a, !0)
      }
      for (var m in f)
          if (f.hasOwnProperty(m))
              a: {
                  var n = m
                    , p = f[m]
                    , q = a;
                  if (q.tagName) {
                      if ("a" === q.tagName.toLowerCase()) {
                          Rk(n, p, q);
                          break a
                      }
                      if ("form" === q.tagName.toLowerCase()) {
                          Qk(n, p, q);
                          break a
                      }
                  }
                  "string" == typeof q && Ok(n, p, q)
              }
  }
  function Rk(a, b, c, d) {
      if (c.href) {
          var e = Ok(a, b, c.href, void 0 === d ? !1 : d);
          hb.test(e) && (c.href = e)
      }
  }
  function Qk(a, b, c) {
      if (c && c.action) {
          var d = (c.method || "").toLowerCase();
          if ("get" === d) {
              for (var e = c.childNodes || [], f = !1, g = 0; g < e.length; g++) {
                  var l = e[g];
                  if (l.name === a) {
                      l.setAttribute("value", b);
                      f = !0;
                      break
                  }
              }
              if (!f) {
                  var m = C.createElement("input");
                  m.setAttribute("type", "hidden");
                  m.setAttribute("name", a);
                  m.setAttribute("value", b);
                  c.appendChild(m)
              }
          } else if ("post" === d) {
              var n = Ok(a, b, c.action);
              hb.test(n) && (c.action = n)
          }
      }
  }
  function vk(a) {
      try {
          var b;
          a: {
              for (var c = a, d = 100; c && 0 < d; ) {
                  if (c.href && c.nodeName.match(/^a(?:rea)?$/i)) {
                      b = c;
                      break a
                  }
                  c = c.parentNode;
                  d--
              }
              b = null
          }
          var e = b;
          if (e) {
              var f = e.protocol;
              "http:" !== f && "https:" !== f || Pk(e, e.hostname)
          }
      } catch (g) {}
  }
  function wk(a) {
      try {
          if (a.action) {
              var b = xf(zf(a.action), "host");
              Pk(a, b)
          }
      } catch (c) {}
  }
  var Sk = function(a, b, c, d) {
      yk();
      zk(a, b, "fragment" === c ? 2 : 1, !!d, !1)
  }
    , Tk = function(a, b) {
      yk();
      zk(a, [wf(z.location, "host", !0)], b, !0, !0)
  }
    , Uk = function() {
      var a = C.location.hostname
        , b = Ck.exec(C.referrer);
      if (!b)
          return !1;
      var c = b[2]
        , d = b[1]
        , e = "";
      if (c) {
          var f = c.split("/")
            , g = f[1];
          e = "s" === g ? decodeURIComponent(f[2]) : decodeURIComponent(g)
      } else if (d) {
          if (0 === d.indexOf("xn--"))
              return !1;
          e = d.replace(/-/g, ".").replace(/\.\./g, "-")
      }
      var l = a.replace(Dk, ""), m = e.replace(Dk, ""), n;
      if (!(n = l === m)) {
          var p = "." + m;
          n = l.substring(l.length - p.length, l.length) === p
      }
      return n
  }
    , Vk = function(a, b) {
      return !1 === a ? !1 : a || b || Uk()
  };
  var Wk = ["1"]
    , Xk = {}
    , Yk = {}
    , $k = function(a) {
      return Xk[Zk(a)]
  }
    , dl = function(a, b) {
      b = void 0 === b ? !0 : b;
      var c = Zk(a.prefix);
      if (!Xk[c])
          if (al(c, a.path, a.domain)) {
              if (Ve(1)) {
                  var d = Yk[Zk(a.prefix)];
                  bl(a, d ? d.id : void 0, d ? d.fg : void 0)
              }
          } else {
              if (Ve(2)) {
                  var e = Bf("auiddc");
                  if (e) {
                      $a("TAGGING", 17);
                      Xk[c] = e;
                      return
                  }
              }
              if (b) {
                  var f = Zk(a.prefix)
                    , g = Xh();
                  if (0 === cl(f, g, a)) {
                      var l = Gb("google_tag_data", {});
                      l._gcl_au || (l._gcl_au = g)
                  }
                  al(c, a.path, a.domain)
              }
          }
  };
  function bl(a, b, c) {
      var d = Zk(a.prefix)
        , e = Xk[d];
      if (e) {
          var f = e.split(".");
          if (2 === f.length) {
              var g = Number(f[1]) || 0;
              if (g) {
                  var l = e;
                  b && (l = e + "." + b + "." + (c ? c : Math.floor(Ha() / 1E3)));
                  cl(d, l, a, 1E3 * g)
              }
          }
      }
  }
  function cl(a, b, c, d) {
      var e = ai(b, "1", c.domain, c.path)
        , f = tk(c, d);
      f.kb = "ad_storage";
      return Th(a, e, f)
  }
  function al(a, b, c) {
      var d = $h(a, b, c, Wk, "ad_storage");
      if (!d)
          return !1;
      el(a, d);
      return !0
  }
  function el(a, b) {
      var c = b.split(".");
      5 === c.length ? (Xk[a] = c.slice(0, 2).join("."),
      Yk[a] = {
          id: c.slice(2, 4).join("."),
          fg: Number(c[4]) || 0
      }) : 3 === c.length ? Yk[a] = {
          id: c.slice(0, 2).join("."),
          fg: Number(c[2]) || 0
      } : Xk[a] = b
  }
  function Zk(a) {
      return (a || "_gcl") + "_au"
  }
  function fl(a) {
      Ug() ? gh(function() {
          Sg("ad_storage") ? a() : hh(a, "ad_storage")
      }, ["ad_storage"]) : a()
  }
  function gl(a) {
      var b = Mk(!0)
        , c = Zk(a.prefix);
      fl(function() {
          var d = b[c];
          if (d) {
              el(c, d);
              var e = 1E3 * Number(Xk[c].split(".")[1]);
              if (e) {
                  $a("TAGGING", 16);
                  var f = tk(a, e);
                  f.kb = "ad_storage";
                  var g = ai(d, "1", a.domain, a.path);
                  Th(c, g, f)
              }
          }
      })
  }
  function hl(a, b, c, d, e) {
      e = e || {};
      var f = function() {
          var g = {}
            , l = $h(a, e.path, e.domain, Wk, "ad_storage");
          l && (g[a] = l);
          return g
      };
      fl(function() {
          Sk(f, b, c, d)
      })
  }
  ;var il = function(a) {
      for (var b = [], c = C.cookie.split(";"), d = new RegExp("^\\s*" + (a || "_gac") + "_(UA-\\d+-\\d+)=\\s*(.+?)\\s*$"), e = 0; e < c.length; e++) {
          var f = c[e].match(d);
          f && b.push({
              vg: f[1],
              value: f[2],
              timestamp: Number(f[2].split(".")[1]) || 0
          })
      }
      b.sort(function(g, l) {
          return l.timestamp - g.timestamp
      });
      return b
  };
  function jl(a, b) {
      var c = il(a)
        , d = {};
      if (!c || !c.length)
          return d;
      for (var e = 0; e < c.length; e++) {
          var f = c[e].value.split(".");
          if (!("1" !== f[0] || b && 3 > f.length || !b && 3 !== f.length) && Number(f[1])) {
              d[c[e].vg] || (d[c[e].vg] = []);
              var g = {
                  version: f[0],
                  timestamp: 1E3 * Number(f[1]),
                  aa: f[2]
              };
              b && 3 < f.length && (g.labels = f.slice(3));
              d[c[e].vg].push(g)
          }
      }
      return d
  }
  ;var kl = /^\w+$/
    , ll = /^[\w-]+$/
    , ml = {
      aw: "_aw",
      dc: "_dc",
      gf: "_gf",
      ha: "_ha",
      gp: "_gp",
      gb: "_gb"
  }
    , nl = function() {
      return Ag().h() && Ug() ? Sg("ad_storage") : !0
  }
    , ol = function(a, b) {
      Tg("ad_storage") ? nl() ? a() : hh(a, "ad_storage") : b ? $a("TAGGING", 3) : gh(function() {
          ol(a, !0)
      }, ["ad_storage"])
  }
    , ql = function(a) {
      return pl(a).map(function(b) {
          return b.aa
      })
  }
    , pl = function(a) {
      var b = [];
      if (!Hh(z) || !C.cookie)
          return b;
      var c = Kh(a, C.cookie, void 0, "ad_storage");
      if (!c || 0 == c.length)
          return b;
      for (var d = {}, e = 0; e < c.length; d = {
          Pd: d.Pd
      },
      e++) {
          var f = rl(c[e]);
          if (null != f) {
              var g = f
                , l = g.version;
              d.Pd = g.aa;
              var m = g.timestamp
                , n = g.labels
                , p = va(b, function(q) {
                  return function(r) {
                      return r.aa === q.Pd
                  }
              }(d));
              p ? (p.timestamp = Math.max(p.timestamp, m),
              p.labels = sl(p.labels, n || [])) : b.push({
                  version: l,
                  aa: d.Pd,
                  timestamp: m,
                  labels: n
              })
          }
      }
      b.sort(function(q, r) {
          return r.timestamp - q.timestamp
      });
      return tl(b)
  };
  function sl(a, b) {
      for (var c = {}, d = [], e = 0; e < a.length; e++)
          c[a[e]] = !0,
          d.push(a[e]);
      for (var f = 0; f < b.length; f++)
          c[b[f]] || d.push(b[f]);
      return d
  }
  function ul(a) {
      return a && "string" == typeof a && a.match(kl) ? a : "_gcl"
  }
  var wl = function() {
      var a = zf(z.location.href)
        , b = xf(a, "query", !1, void 0, "gclid")
        , c = xf(a, "query", !1, void 0, "gclsrc")
        , d = xf(a, "query", !1, void 0, "wbraid")
        , e = xf(a, "query", !1, void 0, "dclid");
      if (!b || !c || !d) {
          var f = a.hash.replace("#", "");
          b = b || uf(f, "gclid");
          c = c || uf(f, "gclsrc");
          d = d || uf(f, "wbraid")
      }
      return vl(b, c, e, d)
  }
    , vl = function(a, b, c, d) {
      var e = {}
        , f = function(g, l) {
          e[l] || (e[l] = []);
          e[l].push(g)
      };
      e.gclid = a;
      e.gclsrc = b;
      e.dclid = c;
      void 0 !== d && ll.test(d) && (e.gbraid = d,
      f(d, "gb"));
      if (void 0 !== a && a.match(ll))
          switch (b) {
          case void 0:
              f(a, "aw");
              break;
          case "aw.ds":
              f(a, "aw");
              f(a, "dc");
              break;
          case "ds":
              f(a, "dc");
              break;
          case "3p.ds":
              f(a, "dc");
              break;
          case "gf":
              f(a, "gf");
              break;
          case "ha":
              f(a, "ha")
          }
      c && f(c, "dc");
      return e
  }
    , yl = function(a) {
      var b = wl();
      ol(function() {
          xl(b, !1, a)
      })
  };
  function xl(a, b, c, d, e) {
      function f(w, x) {
          var y = zl(w, g);
          y && (Th(y, x, l),
          m = !0)
      }
      c = c || {};
      e = e || [];
      var g = ul(c.prefix);
      d = d || Ha();
      var l = tk(c, d, !0);
      l.kb = "ad_storage";
      var m = !1
        , n = Math.round(d / 1E3)
        , p = function(w) {
          var x = ["GCL", n, w];
          0 < e.length && x.push(e.join("."));
          return x.join(".")
      };
      a.aw && f("aw", p(a.aw[0]));
      a.dc && f("dc", p(a.dc[0]));
      a.gf && f("gf", p(a.gf[0]));
      a.ha && f("ha", p(a.ha[0]));
      a.gp && f("gp", p(a.gp[0]));
      if (!m && a.gb) {
          var q = a.gb[0]
            , r = zl("gb", g)
            , t = !1;
          if (!b)
              for (var u = pl(r), v = 0; v < u.length; v++)
                  u[v].aa === q && u[v].labels && 0 < u[v].labels.length && (t = !0);
          t || f("gb", p(q))
      }
  }
  var Bl = function(a, b) {
      var c = Mk(!0);
      ol(function() {
          for (var d = ul(b.prefix), e = 0; e < a.length; ++e) {
              var f = a[e];
              if (void 0 !== ml[f]) {
                  var g = zl(f, d)
                    , l = c[g];
                  if (l) {
                      var m = Math.min(Al(l), Ha()), n;
                      b: {
                          var p = m;
                          if (Hh(z))
                              for (var q = Kh(g, C.cookie, void 0, "ad_storage"), r = 0; r < q.length; ++r)
                                  if (Al(q[r]) > p) {
                                      n = !0;
                                      break b
                                  }
                          n = !1
                      }
                      if (!n) {
                          var t = tk(b, m, !0);
                          t.kb = "ad_storage";
                          Th(g, l, t)
                      }
                  }
              }
          }
          xl(vl(c.gclid, c.gclsrc), !1, b)
      })
  }
    , zl = function(a, b) {
      var c = ml[a];
      if (void 0 !== c)
          return b + c
  }
    , Al = function(a) {
      return 0 !== Cl(a.split(".")).length ? 1E3 * (Number(a.split(".")[1]) || 0) : 0
  };
  function rl(a) {
      var b = Cl(a.split("."));
      return 0 === b.length ? null : {
          version: b[0],
          aa: b[2],
          timestamp: 1E3 * (Number(b[1]) || 0),
          labels: b.slice(3)
      }
  }
  function Cl(a) {
      return 3 > a.length || "GCL" !== a[0] && "1" !== a[0] || !/^\d+$/.test(a[1]) || !ll.test(a[2]) ? [] : a
  }
  var Dl = function(a, b, c, d, e) {
      if (ua(b) && Hh(z)) {
          var f = ul(e)
            , g = function() {
              for (var l = {}, m = 0; m < a.length; ++m) {
                  var n = zl(a[m], f);
                  if (n) {
                      var p = Kh(n, C.cookie, void 0, "ad_storage");
                      p.length && (l[n] = p.sort()[p.length - 1])
                  }
              }
              return l
          };
          ol(function() {
              Sk(g, b, c, d)
          })
      }
  }
    , tl = function(a) {
      return a.filter(function(b) {
          return ll.test(b.aa)
      })
  }
    , El = function(a, b) {
      if (Hh(z)) {
          for (var c = ul(b.prefix), d = {}, e = 0; e < a.length; e++)
              ml[a[e]] && (d[a[e]] = ml[a[e]]);
          ol(function() {
              k(d, function(f, g) {
                  var l = Kh(c + g, C.cookie, void 0, "ad_storage");
                  l.sort(function(t, u) {
                      return Al(u) - Al(t)
                  });
                  if (l.length) {
                      var m = l[0], n = Al(m), p = 0 !== Cl(m.split(".")).length ? m.split(".").slice(3) : [], q = {}, r;
                      r = 0 !== Cl(m.split(".")).length ? m.split(".")[2] : void 0;
                      q[f] = [r];
                      xl(q, !0, b, n, p)
                  }
              })
          })
      }
  };
  function Fl(a, b) {
      for (var c = 0; c < b.length; ++c)
          if (a[b[c]])
              return !0;
      return !1
  }
  var Gl = function(a) {
      function b(e, f, g) {
          g && (e[f] = g)
      }
      if (Ug()) {
          var c = wl();
          if (Fl(c, a)) {
              var d = {};
              b(d, "gclid", c.gclid);
              b(d, "dclid", c.dclid);
              b(d, "gclsrc", c.gclsrc);
              b(d, "wbraid", c.gbraid);
              Tk(function() {
                  return d
              }, 3);
              Tk(function() {
                  var e = {};
                  return e._up = "1",
                  e
              }, 1)
          }
      }
  }
    , Hl = function(a, b, c, d) {
      var e = [];
      c = c || {};
      if (!nl())
          return e;
      var f = pl(a);
      if (!f.length)
          return e;
      for (var g = 0; g < f.length; g++)
          -1 === (f[g].labels || []).indexOf(b) ? e.push(0) : e.push(1);
      if (d)
          return e;
      if (1 !== e[0]) {
          var l = f[0]
            , m = f[0].timestamp
            , n = [l.version, Math.round(m / 1E3), l.aa].concat(l.labels || [], [b]).join(".")
            , p = tk(c, m, !0);
          p.kb = "ad_storage";
          Th(a, n, p)
      }
      return e
  };
  function Il(a, b) {
      var c = ul(b)
        , d = zl(a, c);
      if (!d)
          return 0;
      for (var e = pl(d), f = 0, g = 0; g < e.length; g++)
          f = Math.max(f, e[g].timestamp);
      return f
  }
  function Jl(a) {
      var b = 0, c;
      for (c in a)
          for (var d = a[c], e = 0; e < d.length; e++)
              b = Math.max(b, Number(d[e].timestamp));
      return b
  }
  var Kl = function(a) {
      var b = Math.max(Il("aw", a), Jl(nl() ? jl() : {}));
      return Math.max(Il("gb", a), Jl(nl() ? jl("_gac_gb", !0) : {})) > b
  };
  var Pl = /[A-Z]+/
    , Ql = /\s/
    , Rl = function(a, b) {
      if (h(a)) {
          a = Fa(a);
          var c = a.indexOf("-");
          if (!(0 > c)) {
              var d = a.substring(0, c);
              if (Pl.test(d)) {
                  var e = a.substring(c + 1), f;
                  if (b && R(120)) {
                      var g = function(n) {
                          var p = n.indexOf("/");
                          return 0 > p ? [n] : [n.substring(0, p), n.substring(p + 1)]
                      };
                      f = g(e);
                      if ("DC" === d && 2 === f.length) {
                          var l = g(f[1]);
                          2 === l.length && (f[1] = l[0],
                          f.push(l[1]))
                      }
                  } else {
                      f = e.split("/");
                      for (var m = 0; m < f.length; m++)
                          if (!f[m] || Ql.test(f[m]) && ("AW" !== d || 1 !== m))
                              return
                  }
                  return {
                      id: a,
                      prefix: d,
                      W: d + "-" + f[0],
                      I: f
                  }
              }
          }
      }
  }
    , Tl = function(a, b) {
      for (var c = {}, d = 0; d < a.length; ++d) {
          var e = Rl(a[d], b);
          e && (c[e.id] = e)
      }
      Sl(c);
      var f = [];
      k(c, function(g, l) {
          f.push(l)
      });
      return f
  };
  function Sl(a) {
      var b = [], c;
      for (c in a)
          if (a.hasOwnProperty(c)) {
              var d = a[c];
              "AW" === d.prefix && d.I[1] && b.push(d.W)
          }
      for (var e = 0; e < b.length; ++e)
          delete a[b[e]]
  }
  ;var Ul = function(a, b, c, d) {
      var e = Mb(), f;
      if (1 === e)
          a: {
              var g = De;
              g = g.toLowerCase();
              for (var l = "https://" + g, m = "http://" + g, n = 1, p = C.getElementsByTagName("script"), q = 0; q < p.length && 100 > q; q++) {
                  var r = p[q].src;
                  if (r) {
                      r = r.toLowerCase();
                      if (0 === r.indexOf(m)) {
                          f = 3;
                          break a
                      }
                      1 === n && 0 === r.indexOf(l) && (n = 2)
                  }
              }
              f = n
          }
      else
          f = e;
      return (2 === f || d || "http:" != z.location.protocol ? a : b) + c
  };
  var Wl = function(a, b, c) {
      if (z[a.functionName])
          return b.lg && F(b.lg),
          z[a.functionName];
      var d = Vl();
      z[a.functionName] = d;
      if (a.Je)
          for (var e = 0; e < a.Je.length; e++)
              z[a.Je[e]] = z[a.Je[e]] || Vl();
      a.Re && void 0 === z[a.Re] && (z[a.Re] = c);
      Lb(Ul("https://", "http://", a.sg), b.lg, b.Xk);
      return d
  }
    , Vl = function() {
      var a = function() {
          a.q = a.q || [];
          a.q.push(arguments)
      };
      return a
  }
    , Xl = {
      functionName: "_googWcmImpl",
      Re: "_googWcmAk",
      sg: "www.gstatic.com/wcm/loader.js"
  }
    , Yl = {
      functionName: "_gaPhoneImpl",
      Re: "ga_wpid",
      sg: "www.gstatic.com/gaphone/loader.js"
  }
    , Zl = {
      Hi: "",
      Rj: "5"
  }
    , $l = {
      functionName: "_googCallTrackingImpl",
      Je: [Yl.functionName, Xl.functionName],
      sg: "www.gstatic.com/call-tracking/call-tracking_" + (Zl.Hi || Zl.Rj) + ".js"
  }
    , am = {}
    , bm = function(a, b, c, d) {
      K(22);
      if (c) {
          d = d || {};
          var e = Wl(Xl, d, a)
            , f = {
              ak: a,
              cl: b
          };
          void 0 === d.jb && (f.autoreplace = c);
          e(2, d.jb, f, c, 0, Ga(), d.options)
      }
  }
    , cm = function(a, b, c, d) {
      K(21);
      if (b && c) {
          d = d || {};
          for (var e = {
              countryNameCode: c,
              destinationNumber: b,
              retrievalTime: Ga()
          }, f = 0; f < a.length; f++) {
              var g = a[f];
              am[g.id] || (g && "AW" === g.prefix && !e.adData && 2 <= g.I.length ? (e.adData = {
                  ak: g.I[0],
                  cl: g.I[1]
              },
              am[g.id] = !0) : g && "UA" === g.prefix && !e.gaData && (e.gaData = {
                  gaWpid: g.W
              },
              am[g.id] = !0))
          }
          (e.gaData || e.adData) && Wl($l, d)(d.jb, e, d.options)
      }
  }
    , dm = function() {
      var a = !1;
      return a
  }
    , em = function(a, b) {
      if (a)
          if (ci()) {} else {
              if (h(a)) {
                  var c = Rl(a);
                  if (!c)
                      return;
                  a = c
              }
              var d = void 0
                , e = !1
                , f = S(b, N.g.wj);
              if (f && ua(f)) {
                  d = [];
                  for (var g = 0; g < f.length; g++) {
                      var l = Rl(f[g]);
                      l && (d.push(l),
                      (a.id === l.id || a.id === a.W && a.W === l.W) && (e = !0))
                  }
              }
              if (!d || e) {
                  var m = S(b, N.g.rh), n;
                  if (m) {
                      ua(m) ? n = m : n = [m];
                      var p = S(b, N.g.ph)
                        , q = S(b, N.g.qh)
                        , r = S(b, N.g.sh)
                        , t = S(b, N.g.vj)
                        , u = p || q
                        , v = 1;
                      "UA" !== a.prefix || d || (v = 5);
                      for (var w = 0; w < n.length; w++)
                          if (w < v)
                              if (d)
                                  cm(d, n[w], t, {
                                      jb: u,
                                      options: r
                                  });
                              else if ("AW" === a.prefix && a.I[1])
                                  dm() ? cm([a], n[w], t || "US", {
                                      jb: u,
                                      options: r
                                  }) : bm(a.I[0], a.I[1], n[w], {
                                      jb: u,
                                      options: r
                                  });
                              else if ("UA" === a.prefix)
                                  if (dm())
                                      cm([a], n[w], t || "US", {
                                          jb: u
                                      });
                                  else {
                                      var x = a.W
                                        , y = n[w]
                                        , A = {
                                          jb: u
                                      };
                                      K(23);
                                      if (y) {
                                          A = A || {};
                                          var B = Wl(Yl, A, x)
                                            , D = {};
                                          void 0 !== A.jb ? D.receiver = A.jb : D.replace = y;
                                          D.ga_wpid = x;
                                          D.destination = y;
                                          B(2, Ga(), D)
                                      }
                                  }
                  }
              }
          }
  };
  var fm = function(a, b, c) {
      this.target = a;
      this.eventName = b;
      this.h = c;
      this.m = {};
      this.metadata = J(c.eventMetadata || {});
      this.isAborted = !1
  };
  fm.prototype.copyToHitData = function(a, b) {
      var c = S(this.h, a);
      void 0 !== c ? this.m[a] = c : void 0 !== b && (this.m[a] = b)
  }
  ;
  var gm = function(a, b, c) {
      var d = df(a.target.W);
      return d && d.hasOwnProperty(b) ? d[b] : c
  };
  function hm(a) {
      return {
          getDestinationId: function() {
              return a.target.W
          },
          getEventName: function() {
              return a.eventName
          },
          setEventName: function(b) {
              a.eventName = b
          },
          getHitData: function(b) {
              return a.m[b]
          },
          setHitData: function(b, c) {
              a.m[b] = c
          },
          setHitDataIfNotDefined: function(b, c) {
              void 0 === a.m[b] && (a.m[b] = c)
          },
          copyToHitData: function(b, c) {
              a.copyToHitData(b, c)
          },
          getMetadata: function(b) {
              return a.metadata[b]
          },
          setMetadata: function(b, c) {
              a.metadata[b] = c
          },
          isAborted: function() {
              return a.isAborted
          },
          abort: function() {
              a.isAborted = !0
          },
          getFromEventContext: function(b) {
              return S(a.h, b)
          },
          hm: function() {
              return a
          },
          getHitKeys: function() {
              return Object.keys(a.m)
          }
      }
  }
  ;var Bm = function(a, b, c, d, e, f, g, l, m, n, p, q) {
      this.eventId = a;
      this.priorityId = b;
      this.h = c;
      this.J = d;
      this.m = e;
      this.H = f;
      this.X = g;
      this.B = l;
      this.eventMetadata = m;
      this.K = n;
      this.O = p;
      this.isGtmEvent = q
  }
    , S = function(a, b, c) {
      if (void 0 !== a.h[b])
          return a.h[b];
      if (void 0 !== a.J[b])
          return a.J[b];
      if (void 0 !== a.m[b])
          return a.m[b];
      mj && Cm(a, a.H[b], a.X[b]) && (K(71),
      K(79));
      return void 0 !== a.H[b] ? a.H[b] : void 0 !== a.B[b] ? a.B[b] : c
  }
    , Dm = function(a) {
      function b(g) {
          for (var l = Object.keys(g), m = 0; m < l.length; ++m)
              c[l[m]] = 1
      }
      var c = {};
      b(a.h);
      b(a.J);
      b(a.m);
      b(a.H);
      if (mj)
          for (var d = Object.keys(a.X), e = 0; e < d.length; e++) {
              var f = d[e];
              if ("event" !== f && "gtm" !== f && "tagTypeBlacklist" !== f && !c.hasOwnProperty(f)) {
                  K(71);
                  K(80);
                  break
              }
          }
      return Object.keys(c)
  }
    , Em = function(a, b, c) {
      function d(m) {
          G(m) && k(m, function(n, p) {
              f = !0;
              e[n] = p
          })
      }
      var e = {}
        , f = !1;
      c && 1 !== c || (d(a.B[b]),
      d(a.H[b]),
      d(a.m[b]),
      d(a.J[b]));
      c && 2 !== c || d(a.h[b]);
      if (mj) {
          var g = f
            , l = e;
          e = {};
          f = !1;
          c && 1 !== c || (d(a.B[b]),
          d(a.X[b]),
          d(a.m[b]),
          d(a.J[b]));
          c && 2 !== c || d(a.h[b]);
          if (f !== g || Cm(a, e, l))
              K(71),
              K(81);
          f = g;
          e = l
      }
      return f ? e : void 0
  }
    , Fm = function(a) {
      var b = [N.g.Pc, N.g.Lc, N.g.Mc, N.g.Nc, N.g.Oc, N.g.Qc, N.g.Rc]
        , c = {}
        , d = !1
        , e = function(l) {
          for (var m = 0; m < b.length; m++)
              void 0 !== l[b[m]] && (c[b[m]] = l[b[m]],
              d = !0);
          return d
      };
      if (e(a.h) || e(a.J) || e(a.m))
          return c;
      e(a.H);
      if (mj) {
          var f = c
            , g = d;
          c = {};
          d = !1;
          e(a.X);
          Cm(a, c, f) && (K(71),
          K(82));
          c = f;
          d = g
      }
      if (d)
          return c;
      e(a.B);
      return c
  }
    , Cm = function(a, b, c) {
      if (!mj)
          return !1;
      try {
          if (b === c)
              return !1;
          var d = ac(b);
          if (d !== ac(c) || !(G(b) && G(c) || "array" === d))
              return !0;
          if ("array" === d) {
              if (b.length !== c.length)
                  return !0;
              for (var e = 0; e < b.length; e++)
                  if (Cm(a, b[e], c[e]))
                      return !0
          } else {
              for (var f in c)
                  if (!b.hasOwnProperty(f))
                      return !0;
              for (var g in b)
                  if (!c.hasOwnProperty(g) || Cm(a, b[g], c[g]))
                      return !0
          }
      } catch (l) {
          K(72)
      }
      return !1
  }
    , Gm = function(a, b) {
      this.Fj = a;
      this.Gj = b;
      this.H = {};
      this.Ae = {};
      this.h = {};
      this.J = {};
      this.m = {};
      this.od = {};
      this.B = {};
      this.Kc = function() {}
      ;
      this.Bb = function() {}
      ;
      this.X = !1
  }
    , Hm = function(a, b) {
      a.H = b;
      return a
  }
    , Im = function(a, b) {
      a.Ae = b;
      return a
  }
    , Jm = function(a, b) {
      a.h = b;
      return a
  }
    , Km = function(a, b) {
      a.J = b;
      return a
  }
    , Lm = function(a, b) {
      a.m = b;
      return a
  }
    , Mm = function(a, b) {
      a.od = b;
      return a
  }
    , Nm = function(a, b) {
      a.B = b || {};
      return a
  }
    , Om = function(a, b) {
      a.Kc = b;
      return a
  }
    , Pm = function(a, b) {
      a.Bb = b;
      return a
  }
    , Qm = function(a, b) {
      a.X = b;
      return a
  }
    , Rm = function(a) {
      return new Bm(a.Fj,a.Gj,a.H,a.Ae,a.h,a.J,a.m,a.od,a.B,a.Kc,a.Bb,a.X)
  };
  function Vm(a) {
      var b = S(a.h, N.g.vb)
        , c = S(a.h, N.g.Gb);
      R(107) && b && !c ? (a.eventName !== N.g.ja && a.eventName !== N.g.Yd && K(131),
      a.isAborted = !0) : !b && c && (K(132),
      a.isAborted = !0)
  }
  ;function Xm() {
      return "attribution-reporting"
  }
  function Ym(a) {
      var b;
      b = void 0 === b ? document : b;
      var c;
      return !(null == (c = b.featurePolicy) || !c.allowedFeatures().includes(a))
  }
  ;var Zm = !1;
  function $m() {
      if (Ym("join-ad-interest-group") && sa(Db.joinAdInterestGroup))
          return !0;
      Zm || (Fi('AymqwRC7u88Y4JPvfIF2F37QKylC04248hLCdJAsh8xgOfe/dVJPV3XS3wLFca1ZMVOtnBfVjaCMTVudWM//5g4AAAB7eyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGV0YWdtYW5hZ2VyLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjk1MTY3OTk5LCJpc1RoaXJkUGFydHkiOnRydWV9'),
      Zm = !0);
      return Ym("join-ad-interest-group") && sa(Db.joinAdInterestGroup)
  }
  function an(a, b) {
      var c = void 0;
      try {
          c = C.querySelector('iframe[data-tagging-id="' + b + '"]')
      } catch (e) {}
      if (c) {
          var d = Number(c.dataset.loadTime);
          if (d && 6E4 > Ha() - d) {
              $a("TAGGING", 9);
              return
          }
      } else
          try {
              if (50 <= C.querySelectorAll('iframe[allow="join-ad-interest-group"][data-tagging-id*="-"]').length) {
                  $a("TAGGING", 10);
                  return
              }
          } catch (e) {}
      Nb(a, void 0, {
          allow: "join-ad-interest-group"
      }, {
          taggingId: b,
          loadTime: Ha()
      }, c)
  }
  function bn() {
      return "https://td.doubleclick.net"
  }
  ;var cn = RegExp("^UA-\\d+-\\d+%3A[\\w-]+(?:%2C[\\w-]+)*(?:%3BUA-\\d+-\\d+%3A[\\w-]+(?:%2C[\\w-]+)*)*$")
    , dn = /^~?[\w-]+(?:\.~?[\w-]+)*$/
    , en = /^\d+\.fls\.doubleclick\.net$/
    , fn = /;gac=([^;?]+)/
    , gn = /;gacgb=([^;?]+)/
    , hn = /;gclaw=([^;?]+)/
    , jn = /;gclgb=([^;?]+)/;
  function kn(a, b) {
      if (en.test(C.location.host)) {
          var c = C.location.href.match(b);
          return c && 2 == c.length && c[1].match(cn) ? decodeURIComponent(c[1]) : ""
      }
      var d = [], e;
      for (e in a) {
          for (var f = [], g = a[e], l = 0; l < g.length; l++)
              f.push(g[l].aa);
          d.push(e + ":" + f.join(","))
      }
      return 0 < d.length ? d.join(";") : ""
  }
  var ln = function(a, b, c) {
      var d = nl() ? jl("_gac_gb", !0) : {}, e = [], f = !1, g;
      for (g in d) {
          var l = Hl("_gac_gb_" + g, a, b, c);
          f = f || 0 !== l.length && l.some(function(m) {
              return 1 === m
          });
          e.push(g + ":" + l.join(","))
      }
      return {
          qk: f ? e.join(";") : "",
          pk: kn(d, gn)
      }
  };
  function mn(a, b, c) {
      if (en.test(C.location.host)) {
          var d = C.location.href.match(c);
          if (d && 2 == d.length && d[1].match(dn))
              return [{
                  aa: d[1]
              }]
      } else
          return pl((a || "_gcl") + b);
      return []
  }
  var nn = function(a) {
      return mn(a, "_aw", hn).map(function(b) {
          return b.aa
      }).join(".")
  }
    , on = function(a) {
      return mn(a, "_gb", jn).map(function(b) {
          return b.aa
      }).join(".")
  }
    , pn = function(a, b) {
      var c = Hl((b && b.prefix || "_gcl") + "_gb", a, b);
      return 0 === c.length || c.every(function(d) {
          return 0 === d
      }) ? "" : c.join(".")
  };
  var qn = function() {
      if (sa(z.__uspapi)) {
          var a = "";
          try {
              z.__uspapi("getUSPData", 1, function(b, c) {
                  if (c && b) {
                      var d = b.uspString;
                      d && RegExp("^[\\da-zA-Z-]{1,20}$").test(d) && (a = d)
                  }
              })
          } catch (b) {}
          return a
      }
  };
  var bo = {
      F: {
          Ag: "ads_conversion_hit",
          df: "container_execute_start",
          Dg: "container_setup_end",
          ef: "container_setup_start",
          Cg: "container_execute_end",
          Eg: "container_yield_end",
          ff: "container_yield_start",
          Ch: "event_execute_end",
          Dh: "event_setup_end",
          nd: "event_setup_start",
          Eh: "ga4_conversion_hit",
          pd: "page_load",
          Vl: "pageview",
          Ab: "snippet_load",
          Oh: "tag_callback_error",
          Ph: "tag_callback_failure",
          Qh: "tag_callback_success",
          Rh: "tag_execute_end",
          wc: "tag_execute_start"
      }
  };
  var co = !1
    , eo = "L S Y E TC HTC".split(" ")
    , fo = ["S", "E"]
    , go = ["TS", "TE"];
  var Ho = function(a) {}
    , Io = function(a) {}
    , ho = function(a, b, c, d, e, f) {
      var g;
      g = void 0 === g ? !1 : g;
      var l = {};
      return l
  }
    , io = function(a) {
      var b = !1;
      return b
  }
    , jo = function(a, b) {}
    , Jo = function() {
      var a = {};
      return a
  }
    , Ao = function(a) {
      a = void 0 === a ? !0 : a;
      var b = {};
      return b
  }
    , Ko = function() {}
    , Lo = function(a, b, c) {};
  var Mo = function(a, b) {
      var c, d = z.GooglebQhCsO;
      d || (d = {},
      z.GooglebQhCsO = d);
      c = d;
      if (c[a])
          return !1;
      c[a] = [];
      c[a][0] = b;
      return !0
  };
  var No = function(a, b, c) {
      var d = Ai(a, "fmt");
      if (b) {
          var e = Ai(a, "random")
            , f = Ai(a, "label") || "";
          if (!e)
              return !1;
          var g = Qj(decodeURIComponent(f.replace(/\+/g, " ")) + ":" + decodeURIComponent(e.replace(/\+/g, " ")));
          if (!Mo(g, b))
              return !1
      }
      d && 4 != d && (a = Ci(a, "rfmt", d));
      var l = Ci(a, "fmt", 4);
      Lb(l, function() {
          z.google_noFurtherRedirects && b && b.call && (z.google_noFurtherRedirects = null,
          b())
      }, void 0, c, C.getElementsByTagName("script")[0].parentElement || void 0);
      return !0
  };
  var cp = function() {
      this.h = {}
  }
    , dp = function(a, b, c) {
      null != c && (a.h[b] = c)
  }
    , ep = function(a) {
      return Object.keys(a.h).map(function(b) {
          return encodeURIComponent(b) + "=" + encodeURIComponent(a.h[b])
      }).join("&")
  }
    , gp = function(a, b, c, d) {};
  function ip(a, b) {
      if (a) {
          var c = "" + a;
          0 !== c.indexOf("http://") && 0 !== c.indexOf("https://") && (c = "https://" + c);
          "/" === c[c.length - 1] && (c = c.substring(0, c.length - 1));
          return zf("" + c + b).href
      }
  }
  function jp() {
      return !!ne.He && "SGTM_TOKEN" !== ne.He.split("@@").join("")
  }
  function kp(a) {
      for (var b = lp(), c = fa(b), d = c.next(); !d.done; d = c.next()) {
          var e = S(a, d.value);
          if (e)
              return e
      }
  }
  function lp() {
      var a = [];
      R(113) && a.push(N.g.we);
      a.push(N.g.sc);
      return a
  }
  ;var np = function(a, b, c, d) {
      if (!mp() && !mi(a)) {
          var e = c ? "/gtag/js" : "/gtm.js"
            , f = "?id=" + encodeURIComponent(a) + "&l=" + ne.da
            , g = 0 === a.indexOf("GTM-");
          g || (f += "&cx=c");
          var l = jp();
          l && (f += "&sign=" + ne.He);
          var m = xe || ze ? ip(b, e + f) : void 0;
          if (!m) {
              var n = ne.Xd + e;
              l && Fb && g && (n = Fb.replace(/^(?:https?:\/\/)?/i, "").split(/[?#]/)[0]);
              m = Ul("https://", "http://", n + f)
          }
          var p = ni();
          di().container[a] = {
              state: 1,
              context: d,
              parent: p
          };
          ei({
              ctid: a,
              isDestination: !1
          });
          Lb(m)
      }
  }
    , op = function(a, b, c) {
      var d;
      if (d = !mp()) {
          var e = di().destination[a];
          d = !(e && e.state)
      }
      if (d)
          if (oi())
              di().destination[a] = {
                  state: 0,
                  transportUrl: b,
                  context: c,
                  parent: ni()
              },
              ei({
                  ctid: a,
                  isDestination: !0
              }),
              K(91);
          else {
              var f = "/gtag/destination?id=" + encodeURIComponent(a) + "&l=" + ne.da + "&cx=c";
              jp() && (f += "&sign=" + ne.He);
              var g = xe || ze ? ip(b, f) : void 0;
              g || (g = Ul("https://", "http://", ne.Xd + f));
              di().destination[a] = {
                  state: 1,
                  context: c,
                  parent: ni()
              };
              ei({
                  ctid: a,
                  isDestination: !0
              });
              Lb(g)
          }
  };
  function mp() {
      if (ci()) {
          return !0
      }
      return !1
  }
  ;var pp = new RegExp(/^(.*\.)?(google|youtube|blogger|withgoogle)(\.com?)?(\.[a-z]{2})?\.?$/)
    , qp = {
      cl: ["ecl"],
      customPixels: ["nonGooglePixels"],
      ecl: ["cl"],
      ehl: ["hl"],
      hl: ["ehl"],
      html: ["customScripts", "customPixels", "nonGooglePixels", "nonGoogleScripts", "nonGoogleIframes"],
      customScripts: ["html", "customPixels", "nonGooglePixels", "nonGoogleScripts", "nonGoogleIframes"],
      nonGooglePixels: [],
      nonGoogleScripts: ["nonGooglePixels"],
      nonGoogleIframes: ["nonGooglePixels"]
  }
    , rp = {
      cl: ["ecl"],
      customPixels: ["customScripts", "html"],
      ecl: ["cl"],
      ehl: ["hl"],
      hl: ["ehl"],
      html: ["customScripts"],
      customScripts: ["html"],
      nonGooglePixels: ["customPixels", "customScripts", "html", "nonGoogleScripts", "nonGoogleIframes"],
      nonGoogleScripts: ["customScripts", "html"],
      nonGoogleIframes: ["customScripts", "html", "nonGoogleScripts"]
  }
    , sp = "google customPixels customScripts html nonGooglePixels nonGoogleScripts nonGoogleIframes".split(" ")
    , vp = function(a) {
      var b = Pe("gtm.allowlist") || Pe("gtm.whitelist");
      b && K(9);
      ve && (b = ["google", "gtagfl", "lcl", "zone"]);
      tp() && (ve ? K(116) : K(117),
      up && (b = [],
      window.console && window.console.log && window.console.log("GTM blocked. See go/13687728.")));
      var c = b && Ma(Ea(b), qp)
        , d = Pe("gtm.blocklist") || Pe("gtm.blacklist");
      d || (d = Pe("tagTypeBlacklist")) && K(3);
      d ? K(8) : d = [];
      tp() && (d = Ea(d),
      d.push("nonGooglePixels", "nonGoogleScripts", "sandboxedScripts"));
      0 <= Ea(d).indexOf("google") && K(2);
      var e = d && Ma(Ea(d), rp)
        , f = {};
      return function(g) {
          var l = g && g[gc.zb];
          if (!l || "string" != typeof l)
              return !0;
          l = l.replace(/^_*/, "");
          if (void 0 !== f[l])
              return f[l];
          var m = He[l] || []
            , n = a(l, m);
          if (R(117)) {
              var p, q = T.Ua || "_" + T.C, r, t = oe.r;
              t || (t = {
                  container: {}
              },
              oe.r = t);
              r = t;
              var u = r.container[q];
              u || (u = {
                  entity: []
              },
              r.container[q] = u);
              p = u.entity;
              for (var v = 0; v < p.length; v++)
                  try {
                      n = n && p[v](l, m)
                  } catch (I) {
                      n = !1
                  }
          }
          if (b) {
              var w;
              if (w = n)
                  a: {
                      if (0 > c.indexOf(l))
                          if (m && 0 < m.length)
                              for (var x = 0; x < m.length; x++) {
                                  if (0 > c.indexOf(m[x])) {
                                      K(11);
                                      w = !1;
                                      break a
                                  }
                              }
                          else {
                              w = !1;
                              break a
                          }
                      w = !0
                  }
              n = w
          }
          var y = !1;
          if (d) {
              var A = 0 <= e.indexOf(l);
              if (A)
                  y = A;
              else {
                  var B = za(e, m || []);
                  B && K(10);
                  y = B
              }
          }
          var D = !n || y;
          D || !(0 <= m.indexOf("sandboxedScripts")) || c && -1 !== c.indexOf("sandboxedScripts") || (D = za(e, sp));
          return f[l] = D
      }
  }
    , up = !1;
  var tp = function() {
      return pp.test(z.location && z.location.hostname)
  };
  var wp = {
      initialized: 11,
      complete: 12,
      interactive: 13
  }
    , xp = {}
    , yp = Object.freeze((xp[N.g.Ma] = !0,
  xp))
    , zp = 0 <= C.location.search.indexOf("?gtm_diagnostics=") || 0 <= C.location.search.indexOf("&gtm_diagnostics=")
    , Bp = function(a, b, c) {
      if (mj && "config" === a && !(1 < Rl(b).I.length)) {
          var d, e = Gb("google_tag_data", {});
          e.td || (e.td = {});
          d = e.td;
          var f = J(c.H);
          J(c.h, f);
          var g = [], l;
          for (l in d) {
              var m = Ap(d[l], f);
              m.length && (zp && console.log(m),
              g.push(l))
          }
          if (g.length) {
              if (g.length) {
                  var n = b + "*" + g.join(".");
                  vj = vj ? vj + "!" + n : "&tdc=" + n
              }
              $a("TAGGING", wp[C.readyState] || 14)
          }
          d[b] = f
      }
  };
  function Cp(a, b) {
      var c = {}, d;
      for (d in b)
          b.hasOwnProperty(d) && (c[d] = !0);
      for (var e in a)
          a.hasOwnProperty(e) && (c[e] = !0);
      return c
  }
  function Ap(a, b, c, d) {
      c = void 0 === c ? {} : c;
      d = void 0 === d ? "" : d;
      if (a === b)
          return [];
      var e = function(q, r) {
          var t = r[q];
          return void 0 === t ? yp[q] : t
      }, f;
      for (f in Cp(a, b)) {
          var g = (d ? d + "." : "") + f
            , l = e(f, a)
            , m = e(f, b)
            , n = "object" === ac(l) || "array" === ac(l)
            , p = "object" === ac(m) || "array" === ac(m);
          if (n && p)
              Ap(l, m, c, g);
          else if (n || p || l !== m)
              c[g] = !0
      }
      return Object.keys(c)
  }
  ;var Dp = !1
    , Ep = 0
    , Fp = [];
  function Gp(a) {
      if (!Dp) {
          var b = C.createEventObject
            , c = "complete" == C.readyState
            , d = "interactive" == C.readyState;
          if (!a || "readystatechange" != a.type || c || !b && d) {
              Dp = !0;
              for (var e = 0; e < Fp.length; e++)
                  F(Fp[e])
          }
          Fp.push = function() {
              for (var f = 0; f < arguments.length; f++)
                  F(arguments[f]);
              return 0
          }
      }
  }
  function Hp() {
      if (!Dp && 140 > Ep) {
          Ep++;
          try {
              C.documentElement.doScroll("left"),
              Gp()
          } catch (a) {
              z.setTimeout(Hp, 50)
          }
      }
  }
  var Ip = function(a) {
      Dp ? a() : Fp.push(a)
  };
  var Jp = function(a, b) {
      return {
          entityType: 1,
          indexInOriginContainer: a,
          nameInOriginContainer: b,
          originContainerId: T.C
      }
  };
  function Kp(a, b) {
      if (data.entities && data.entities[a])
          return data.entities[a][b]
  }
  ;var Mp = function(a, b) {
      this.h = !1;
      this.H = [];
      this.J = {
          tags: []
      };
      this.X = !1;
      this.m = this.B = 0;
      Lp(this, a, b)
  }
    , Np = function(a, b, c, d) {
      if (se.hasOwnProperty(b) || "__zone" === b)
          return -1;
      var e = {};
      G(d) && (e = J(d, e));
      e.id = c;
      e.status = "timeout";
      return a.J.tags.push(e) - 1
  }
    , Op = function(a, b, c, d) {
      var e = a.J.tags[b];
      e && (e.status = c,
      e.executionTime = d)
  }
    , Pp = function(a) {
      if (!a.h) {
          for (var b = a.H, c = 0; c < b.length; c++)
              b[c]();
          a.h = !0;
          a.H.length = 0
      }
  }
    , Lp = function(a, b, c) {
      void 0 !== b && Qp(a, b);
      c && z.setTimeout(function() {
          return Pp(a)
      }, Number(c))
  }
    , Qp = function(a, b) {
      var c = Ja(function() {
          return F(function() {
              b(T.C, a.J)
          })
      });
      a.h ? c() : a.H.push(c)
  }
    , Rp = function(a) {
      a.B++;
      return Ja(function() {
          a.m++;
          a.X && a.m >= a.B && Pp(a)
      })
  }
    , Sp = function(a) {
      a.X = !0;
      a.m >= a.B && Pp(a)
  };
  var Tp = {}
    , Vp = function() {
      return z[Up()]
  }
    , Wp = !1;
  var Xp = function(a) {
      z.GoogleAnalyticsObject || (z.GoogleAnalyticsObject = a || "ga");
      var b = z.GoogleAnalyticsObject;
      if (z[b])
          z.hasOwnProperty(b);
      else {
          var c = function() {
              c.q = c.q || [];
              c.q.push(arguments)
          };
          c.l = Number(Ga());
          z[b] = c
      }
      return z[b]
  }
    , qq = function(a) {
      if (Ug()) {
          var b = Vp();
          b(a + "require", "linker");
          b(a + "linker:passthrough", !0)
      }
  };
  function Up() {
      return z.GoogleAnalyticsObject || "ga"
  }
  var Eq = function(a) {}
    , Fq = function(a, b) {
      return function() {
          var c = Vp()
            , d = c && c.getByName && c.getByName(a);
          if (d) {
              var e = d.get("sendHitTask");
              d.set("sendHitTask", function(f) {
                  var g = f.get("hitPayload")
                    , l = f.get("hitCallback")
                    , m = 0 > g.indexOf("&tid=" + b);
                  m && (f.set("hitPayload", g.replace(/&tid=UA-[0-9]+-[0-9]+/, "&tid=" + b), !0),
                  f.set("hitCallback", void 0, !0));
                  e(f);
                  m && (f.set("hitPayload", g, !0),
                  f.set("hitCallback", l, !0),
                  f.set("_x_19", void 0, !0),
                  e(f))
              })
          }
      }
  };
  var Kq = {};
  function Lq(a, b) {
      mj && (Kq[a] = Kq[a] || {},
      Kq[a][b] = (Kq[a][b] || 0) + 1)
  }
  function Mq(a) {
      for (var b = a.eventId, c = a.zg, d = Object.entries(Kq[b] || {}), e = [], f = 0; f < d.length; f++) {
          var g = fa(d[f])
            , l = g.next().value
            , m = g.next().value;
          e.push("" + l + m)
      }
      c && delete Kq[b];
      return e.length ? "&md=" + e.join(".") : ""
  }
  ;var Nq = {}
    , Oq = {
      aev: "1",
      c: "2",
      jsm: "3",
      v: "4",
      j: "5",
      smm: "6",
      rmm: "7",
      input: "8"
  };
  function Pq(a, b, c) {
      if (mj) {
          Nq[a] = Nq[a] || [];
          var d = Oq[b] || "0", e;
          e = c instanceof z.Element ? "1" : c instanceof z.Event ? "2" : c instanceof z.RegExp ? "3" : c === z ? "4" : c === C ? "5" : c instanceof z.Promise ? "6" : c instanceof z.Storage ? "7" : c instanceof z.Date ? "8" : c instanceof z.History ? "9" : c instanceof z.Performance ? "a" : c instanceof z.Crypto ? "b" : c instanceof z.Location ? "c" : c instanceof z.Navigator ? "d" : "object" !== typeof c || G(c) ? "0" : "e";
          Nq[a].push("" + d + e)
      }
  }
  function Qq(a) {
      var b = a.eventId
        , c = Nq[b] || [];
      if (!c.length)
          return "";
      a.zg && delete Nq[b];
      return "&pcr=" + c.join(".")
  }
  ;function Rq(a, b, c, d) {
      var e = Hc[a]
        , f = Sq(a, b, c, d);
      if (!f)
          return null;
      var g = Rc(e[gc.Nh], c, []);
      if (g && g.length) {
          var l = g[0];
          f = Rq(l.index, {
              K: f,
              O: 1 === l.di ? b.terminate : f,
              terminate: b.terminate
          }, c, d)
      }
      return f
  }
  function Sq(a, b, c, d) {
      function e() {
          if (f[gc.Lj])
              l();
          else {
              var w = Sc(f, c, [])
                , x = w[gc.Ii];
              if (null != x)
                  for (var y = 0; y < x.length; y++)
                      if (!Sg(x[y])) {
                          l();
                          return
                      }
              var A = Np(c.Lb, String(f[gc.zb]), Number(f[gc.ud]), w[gc.Mj])
                , B = !1;
              w.vtp_gtmOnSuccess = function() {
                  if (!B) {
                      B = !0;
                      var E = Ha() - H;
                      Kj(c.id, Hc[a], "5");
                      Op(c.Lb, A, "success", E);
                      R(70) && Lo(c, f, bo.F.Qh);
                      g()
                  }
              }
              ;
              w.vtp_gtmOnFailure = function() {
                  if (!B) {
                      B = !0;
                      var E = Ha() - H;
                      Kj(c.id, Hc[a], "6");
                      Op(c.Lb, A, "failure", E);
                      R(70) && Lo(c, f, bo.F.Ph);
                      l()
                  }
              }
              ;
              w.vtp_gtmTagId = f.tag_id;
              w.vtp_gtmEventId = c.id;
              c.priorityId && (w.vtp_gtmPriorityId = c.priorityId);
              Kj(c.id, f, "1");
              var D = function() {
                  var E = Ha() - H;
                  Kj(c.id, f, "7");
                  Op(c.Lb, A, "exception", E);
                  R(70) && Lo(c, f, bo.F.Oh);
                  B || (B = !0,
                  l())
              };
              if (R(70)) {
                  var I = ho(bo.F.wc, T.C, c.id, Number(f[gc.ud]), c.name, fj(f));
                  io(I)
              }
              var H = Ha();
              try {
                  Qc(w, {
                      event: c,
                      index: a,
                      type: 1
                  })
              } catch (E) {
                  D(E)
              }
              R(70) && Lo(c, f, bo.F.Rh)
          }
      }
      var f = Hc[a]
        , g = b.K
        , l = b.O
        , m = b.terminate;
      if (c.Yf(f))
          return null;
      var n = Rc(f[gc.Sh], c, []);
      if (n && n.length) {
          var p = n[0]
            , q = Rq(p.index, {
              K: g,
              O: l,
              terminate: m
          }, c, d);
          if (!q)
              return null;
          g = q;
          l = 2 === p.di ? m : q
      }
      if (f[gc.Jh] || f[gc.Oj]) {
          var r = f[gc.Jh] ? Ic : c.Dl
            , t = g
            , u = l;
          if (!r[a]) {
              e = Ja(e);
              var v = Tq(a, r, e);
              g = v.K;
              l = v.O
          }
          return function() {
              r[a](t, u)
          }
      }
      return e
  }
  function Tq(a, b, c) {
      var d = []
        , e = [];
      b[a] = Uq(d, e, c);
      return {
          K: function() {
              b[a] = Vq;
              for (var f = 0; f < d.length; f++)
                  d[f]()
          },
          O: function() {
              b[a] = Wq;
              for (var f = 0; f < e.length; f++)
                  e[f]()
          }
      }
  }
  function Uq(a, b, c) {
      return function(d, e) {
          a.push(d);
          b.push(e);
          c()
      }
  }
  function Vq(a) {
      a()
  }
  function Wq(a, b) {
      b()
  }
  ;var Yq = function(a, b) {
      return 1 === arguments.length ? Xq("config", a) : Xq("config", a, b)
  }
    , Zq = function(a, b, c) {
      c = c || {};
      c[N.g.Kb] = a;
      return Xq("event", b, c)
  };
  function Xq(a) {
      return arguments
  }
  var $q = function() {
      this.h = [];
      this.m = []
  };
  $q.prototype.enqueue = function(a, b, c) {
      var d = this.h.length + 1;
      a["gtm.uniqueEventId"] = b;
      a["gtm.priorityId"] = d;
      c.eventId = b;
      c.fromContainerExecution = !0;
      c.priorityId = d;
      var e = {
          message: a,
          notBeforeEventId: b,
          priorityId: d,
          messageContext: c
      };
      this.h.push(e);
      for (var f = 0; f < this.m.length; f++)
          try {
              this.m[f](e)
          } catch (g) {}
  }
  ;
  $q.prototype.listen = function(a) {
      this.m.push(a)
  }
  ;
  $q.prototype.get = function() {
      for (var a = {}, b = 0; b < this.h.length; b++) {
          var c = this.h[b]
            , d = a[c.notBeforeEventId];
          d || (d = [],
          a[c.notBeforeEventId] = d);
          d.push(c)
      }
      return a
  }
  ;
  $q.prototype.prune = function(a) {
      for (var b = [], c = [], d = 0; d < this.h.length; d++) {
          var e = this.h[d];
          e.notBeforeEventId === a ? b.push(e) : c.push(e)
      }
      this.h = c;
      return b
  }
  ;
  var br = function(a, b, c) {
      ar().enqueue(a, b, c)
  }
    , dr = function() {
      var a = cr;
      ar().listen(a)
  };
  function ar() {
      var a = oe.mb;
      a || (a = new $q,
      oe.mb = a);
      return a
  }
  var lr = function(a) {
      var b = oe.zones;
      return b ? b.getIsAllowedFn(hi(), a) : function() {
          return !0
      }
  }
    , mr = function(a) {
      var b = oe.zones;
      return b ? b.isActive(hi(), a) : !0
  };
  var pr = function(a, b) {
      for (var c = [], d = 0; d < Hc.length; d++)
          if (a[d]) {
              var e = Hc[d];
              var f = Rp(b.Lb);
              try {
                  var g = Rq(d, {
                      K: f,
                      O: f,
                      terminate: f
                  }, b, d);
                  if (g) {
                      var l = e["function"];
                      if (!l)
                          throw "Error: No function name given for function call.";
                      var m = Jc[l];
                      c.push({
                          Ai: d,
                          oi: (m ? m.priorityOverride || 0 : 0) || Kp(e[gc.zb], 1) || 0,
                          execute: g
                      })
                  } else
                      nr(d, b),
                      f()
              } catch (p) {
                  f()
              }
          }
      c.sort(or);
      for (var n = 0; n < c.length; n++)
          c[n].execute();
      return 0 < c.length
  };
  function or(a, b) {
      var c, d = b.oi, e = a.oi;
      c = d > e ? 1 : d < e ? -1 : 0;
      var f;
      if (0 !== c)
          f = c;
      else {
          var g = a.Ai
            , l = b.Ai;
          f = g > l ? 1 : g < l ? -1 : 0
      }
      return f
  }
  function nr(a, b) {
      if (mj) {
          var c = function(d) {
              var e = b.Yf(Hc[d]) ? "3" : "4"
                , f = Rc(Hc[d][gc.Nh], b, []);
              f && f.length && c(f[0].index);
              Kj(b.id, Hc[d], e);
              var g = Rc(Hc[d][gc.Sh], b, []);
              g && g.length && c(g[0].index)
          };
          c(a)
      }
  }
  var sr = !1, qr;
  var xr = function(a) {
      var b = a["gtm.uniqueEventId"]
        , c = a["gtm.priorityId"]
        , d = a.event;
      if (R(70)) {
          var e = ho(bo.F.nd, T.C, b, void 0, d);
          io(e)
      }
      if ("gtm.js" === d) {
          if (sr)
              return !1;
          sr = !0
      }
      var f, g = !1;
      if (mr(b))
          f = lr(b);
      else {
          if ("gtm.js" !== d && "gtm.init" !== d && "gtm.init_consent" !== d)
              return !1;
          g = !0;
          f = lr(Number.MAX_SAFE_INTEGER)
      }
      Jj(b, d);
      var l = a.eventCallback
        , m = a.eventTimeout
        , n = {
          id: b,
          priorityId: c,
          name: d,
          Yf: vp(f),
          Dl: [],
          ji: function() {
              K(6);
              $a("HEALTH", 0)
          },
          Wh: tr(),
          Xh: ur(b),
          Lb: new Mp(function() {
              if (R(70)) {
                  var v = ho(bo.F.Ch, T.C, b, void 0, d);
                  if (io(v)) {
                      var w = ho(bo.F.nd, T.C, b, void 0, d);
                      jo(v, w)
                  }
                  if ("gtm.load" === d) {
                      var x = ho(bo.F.Cg, T.C);
                      if (io(x)) {
                          var y = ho(bo.F.df, T.C);
                          jo(x, y)
                      }
                      Ko();
                  }
              }
              l && l.apply(l, [].slice.call(arguments, 0))
          }
          ,m)
      };
      R(119) && (n.vi = Lq);
      var p = Wc(n);
      g && (p = vr(p));
      if (R(70)) {
          var q = ho(bo.F.Dh, T.C, b, void 0, d);
          if (io(q)) {
              var r = ho(bo.F.nd, T.C, b, void 0, d);
              jo(q, r)
          }
      }
      var t = pr(p, n)
        , u = !1;
      Sp(n.Lb);
      "gtm.js" !== d && "gtm.sync" !== d || Eq(T.C);
      return wr(p, t) || u
  };
  function ur(a) {
      return function(b) {
          cc(b) || Pq(a, "input", b)
      }
  }
  function tr() {
      var a = {};
      a.event = Te("event", 1);
      a.ecommerce = Te("ecommerce", 1);
      a.gtm = Te("gtm");
      a.eventModel = Te("eventModel");
      return a
  }
  function vr(a) {
      for (var b = [], c = 0; c < a.length; c++)
          if (a[c]) {
              var d = String(Hc[c][gc.zb]);
              if (re[d] || void 0 !== Hc[c][gc.Pj] || Ie[d] || Kp(d, 2))
                  b[c] = !0
          }
      return b
  }
  function wr(a, b) {
      if (!b)
          return b;
      for (var c = 0; c < a.length; c++)
          if (a[c] && Hc[c] && !se[String(Hc[c][gc.zb])])
              return !0;
      return !1
  }
  var zr = function(a, b, c, d) {
      var e = Rl(c, d.isGtmEvent);
      e && yr.push("event", [b, a], e, d)
  }
    , Ar = function(a, b, c, d) {
      var e = Rl(c, d.isGtmEvent);
      e && yr.push("get", [a, b], e, d)
  }
    , Br = function() {
      this.status = 1;
      this.H = {};
      this.h = {};
      this.J = {};
      this.X = null;
      this.B = {};
      this.m = !1
  }
    , Cr = function(a, b, c, d) {
      var e = Ha();
      this.type = a;
      this.B = e;
      this.h = b;
      this.m = c;
      this.messageContext = d
  }
    , Dr = function() {
      this.m = {};
      this.B = {};
      this.h = []
  }
    , Er = function(a, b) {
      var c = b.W;
      return a.m[c] = a.m[c] || new Br
  }
    , Fr = function(a, b, c, d) {
      if (d.h) {
          var e = Er(a, d.h)
            , f = e.X;
          if (f) {
              var g = J(c)
                , l = J(e.H[d.h.id])
                , m = J(e.B)
                , n = J(e.h)
                , p = J(a.B)
                , q = {};
              if (mj)
                  try {
                      q = J(Me)
                  } catch (v) {
                      K(72)
                  }
              var r = d.h.prefix
                , t = function(v) {
                  Lj(d.messageContext.eventId, r, v);
                  var w = g[N.g.mc];
                  w && F(w)
              }
                , u = Rm(Qm(Pm(Om(Nm(Lm(Km(Mm(Jm(Im(Hm(new Gm(d.messageContext.eventId,d.messageContext.priorityId), g), l), m), n), p), q), d.messageContext.eventMetadata), function() {
                  if (t) {
                      var v = t;
                      t = void 0;
                      v("2")
                  }
              }), function() {
                  if (t) {
                      var v = t;
                      t = void 0;
                      v("3")
                  }
              }), !!d.messageContext.isGtmEvent));
              try {
                  Lj(d.messageContext.eventId, r, "1"),
                  Bp(d.type, d.h.id, u),
                  f(d.h.id, b, d.B, u)
              } catch (v) {
                  Lj(d.messageContext.eventId, r, "4")
              }
          }
      }
  };
  Dr.prototype.register = function(a, b, c) {
      var d = Er(this, a);
      3 !== d.status && (d.X = b,
      d.status = 3,
      c && (J(d.h, c),
      d.h = c),
      this.flush())
  }
  ;
  Dr.prototype.push = function(a, b, c, d) {
      void 0 !== c && (1 === Er(this, c).status && (Er(this, c).status = 2,
      this.push("require", [{}], c, {})),
      Er(this, c).m && (d.deferrable = !1));
      this.h.push(new Cr(a,c,b,d));
      d.deferrable || this.flush()
  }
  ;
  Dr.prototype.flush = function(a) {
      for (var b = this, c = [], d = !1, e = {}; this.h.length; ) {
          var f = this.h[0]
            , g = f.h;
          if (f.messageContext.deferrable)
              !g || Er(this, g).m ? (f.messageContext.deferrable = !1,
              this.h.push(f)) : c.push(f),
              this.h.shift();
          else {
              switch (f.type) {
              case "require":
                  if (3 !== Er(this, g).status && !a) {
                      this.h.push.apply(this.h, c);
                      return
                  }
                  break;
              case "set":
                  k(f.m[0], function(r, t) {
                      J(Na(r, t), b.B)
                  });
                  break;
              case "config":
                  var l = Er(this, g);
                  e.lb = {};
                  k(f.m[0], function(r) {
                      return function(t, u) {
                          J(Na(t, u), r.lb)
                      }
                  }(e));
                  var m = !!e.lb[N.g.dd];
                  delete e.lb[N.g.dd];
                  var n = g.W === g.id;
                  m || (n ? l.B = {} : l.H[g.id] = {});
                  l.m && m || Fr(this, N.g.ja, e.lb, f);
                  l.m = !0;
                  n ? J(e.lb, l.B) : (J(e.lb, l.H[g.id]),
                  K(70));
                  d = !0;
                  break;
              case "event":
                  e.Od = {};
                  k(f.m[0], function(r) {
                      return function(t, u) {
                          J(Na(t, u), r.Od)
                      }
                  }(e));
                  Fr(this, f.m[1], e.Od, f);
                  break;
              case "get":
                  var p = {}
                    , q = (p[N.g.La] = f.m[0],
                  p[N.g.ab] = f.m[1],
                  p);
                  Fr(this, N.g.Ea, q, f)
              }
              this.h.shift();
              Gr(this, f)
          }
          e = {
              lb: e.lb,
              Od: e.Od
          }
      }
      this.h.push.apply(this.h, c);
      d && this.flush()
  }
  ;
  var Gr = function(a, b) {
      if ("require" !== b.type)
          if (b.h)
              for (var c = Er(a, b.h).J[b.type] || [], d = 0; d < c.length; d++)
                  c[d]();
          else
              for (var e in a.m)
                  if (a.m.hasOwnProperty(e)) {
                      var f = a.m[e];
                      if (f && f.J)
                          for (var g = f.J[b.type] || [], l = 0; l < g.length; l++)
                              g[l]()
                  }
  }
    , Hr = function(a, b) {
      var c = yr
        , d = J(b);
      J(Er(c, a).h, d);
      Er(c, a).h = d
  }
    , yr = new Dr;
  var Ir = {}
    , Jr = {}
    , Kr = function(a, b) {
      for (var c = [], d = [], e = {}, f = 0; f < a.length; e = {
          Td: e.Td,
          Qd: e.Qd
      },
      f++) {
          var g = a[f];
          if (0 <= g.indexOf("-"))
              e.Td = Rl(g, b),
              e.Td && (va(ii(), function(q) {
                  return function(r) {
                      return q.Td.W === r
                  }
              }(e)) ? c.push(g) : d.push(g));
          else {
              var l = Ir[g] || [];
              e.Qd = {};
              l.forEach(function(q) {
                  return function(r) {
                      return q.Qd[r] = !0
                  }
              }(e));
              for (var m = hi(), n = 0; n < m.length; n++)
                  if (e.Qd[m[n]]) {
                      c = c.concat(ii());
                      break
                  }
              var p = Jr[g] || [];
              p.length && (c = c.concat(p))
          }
      }
      return {
          Uk: c,
          Wk: d
      }
  }
    , Lr = function(a) {
      k(Ir, function(b, c) {
          var d = c.indexOf(a);
          0 <= d && c.splice(d, 1)
      })
  }
    , Mr = function(a) {
      k(Jr, function(b, c) {
          var d = c.indexOf(a);
          0 <= d && c.splice(d, 1)
      })
  };
  var Nr = "HA GF G UA AW DC MC".split(" ")
    , Or = !1
    , Pr = !1;
  function Qr(a, b) {
      a.hasOwnProperty("gtm.uniqueEventId") || Object.defineProperty(a, "gtm.uniqueEventId", {
          value: Je()
      });
      b.eventId = a["gtm.uniqueEventId"];
      b.priorityId = a["gtm.priorityId"];
      return {
          eventId: b.eventId,
          priorityId: b.priorityId
      }
  }
  function Rr(a) {
      return !!(a && a.parent && a.context && 1 === a.context.source && 0 !== a.parent.ctid.indexOf("GTM-"))
  }
  var Sr = void 0
    , Tr = void 0
    , Ur = !1;
  function Vr(a) {
      for (var b = lp(), c = fa(b), d = c.next(); !d.done; d = c.next()) {
          var e = d.value
            , f = a && a[e] || yr.B[e];
          if (f)
              return f
      }
  }
  var Wr = {
      config: function(a, b) {
          var c = Qr(a, b);
          if (!(2 > a.length) && h(a[1])) {
              var d = {};
              if (2 < a.length) {
                  if (void 0 != a[2] && !G(a[2]) || 3 < a.length)
                      return;
                  d = a[2]
              }
              var e = Rl(a[1], b.isGtmEvent);
              if (e) {
                  if (!Ur) {
                      var f;
                      a: {
                          if (!T.Ce) {
                              var g = ji(ni()), l;
                              if (Rr(g))
                                  for (var m = g.parent; m; ) {
                                      l = m.isDestination;
                                      var n = ji(m);
                                      if (!Rr(n)) {
                                          f = {
                                              sl: n,
                                              Tk: l
                                          };
                                          break a
                                      }
                                      m = n.parent
                                  }
                          }
                          f = void 0
                      }
                      var p = f;
                      p && (Sr = p.sl,
                      Tr = p.Tk);
                      Ur = !0
                  }
                  Jj(c.eventId, "gtag.config");
                  var q = e.W
                    , r = e.id !== q;
                  if (r ? -1 === ii().indexOf(q) : -1 === hi().indexOf(q)) {
                      if (!R(61) || !d[N.g.vb]) {
                          var t = Vr(d);
                          r ? op(q, t, {
                              source: 2,
                              fromContainerExecution: b.fromContainerExecution
                          }) : (void 0 !== Sr && -1 !== Sr.containers.indexOf(q) && K(129),
                          np(q, t, !0, {
                              source: 2,
                              fromContainerExecution: b.fromContainerExecution
                          }))
                      }
                  } else {
                      if (ue && !r && !d[N.g.dd]) {
                          var u = Pr;
                          Pr = !0;
                          if (u)
                              return
                      }
                      Or || K(43);
                      if (!b.noTargetGroup)
                          if (r) {
                              Mr(e.id);
                              var v = e.id
                                , w = d[N.g.se] || "default";
                              w = String(w).split(",");
                              for (var x = 0; x < w.length; x++) {
                                  var y = Jr[w[x]] || [];
                                  Jr[w[x]] = y;
                                  0 > y.indexOf(v) && y.push(v)
                              }
                          } else {
                              Lr(e.id);
                              var A = e.id
                                , B = d[N.g.se] || "default";
                              B = B.toString().split(",");
                              for (var D = 0; D < B.length; D++) {
                                  var I = Ir[B[D]] || [];
                                  Ir[B[D]] = I;
                                  0 > I.indexOf(A) && I.push(A)
                              }
                          }
                      delete d[N.g.se];
                      var H = b.eventMetadata || {};
                      H.hasOwnProperty("is_external_event") || (H.is_external_event = !b.fromContainerExecution);
                      b.eventMetadata = H;
                      delete d[N.g.mc];
                      var E = r ? [e.id] : ii();
                      Sr && (K(128),
                      Tr && K(130));
                      for (var L = 0; L < E.length; L++) {
                          var M = d
                            , Y = J(b)
                            , V = Rl(E[L], Y.isGtmEvent);
                          V && yr.push("config", [M], V, Y)
                      }
                  }
              }
          }
      },
      consent: function(a, b) {
          if (3 === a.length) {
              K(39);
              var c = Qr(a, b)
                , d = a[1];
              "default" === d ? rh(a[2]) : "update" === d ? sh(a[2], c) : "declare" === d ? b.fromContainerExecution && qh(a[2]) : "core_platform_services" === d && th(a[2])
          }
      },
      event: function(a, b) {
          var c = a[1];
          if (!(2 > a.length) && h(c)) {
              var d;
              if (2 < a.length) {
                  if (!G(a[2]) && void 0 != a[2] || 3 < a.length)
                      return;
                  d = a[2]
              }
              var e = d
                , f = {}
                , g = (f.event = c,
              f);
              e && (g.eventModel = J(e),
              e[N.g.mc] && (g.eventCallback = e[N.g.mc]),
              e[N.g.me] && (g.eventTimeout = e[N.g.me]));
              var l = Qr(a, b)
                , m = l.eventId
                , n = l.priorityId;
              g["gtm.uniqueEventId"] = m;
              n && (g["gtm.priorityId"] = n);
              if ("optimize.callback" === c)
                  return g.eventModel = g.eventModel || {},
                  g;
              var p;
              var q = d
                , r = q && q[N.g.Kb];
              void 0 === r && (r = Pe(N.g.Kb, 2),
              void 0 === r && (r = "default"));
              if (h(r) || ua(r)) {
                  var t;
                  b.isGtmEvent && R(120) ? t = h(r) ? [r] : r : t = r.toString().replace(/\s+/g, "").split(",");
                  var u = Kr(t, b.isGtmEvent)
                    , v = u.Uk
                    , w = u.Wk;
                  if (w.length)
                      for (var x = Vr(q), y = 0; y < w.length; y++) {
                          var A = Rl(w[y], b.isGtmEvent);
                          A && op(A.W, x, {
                              source: 3,
                              fromContainerExecution: b.fromContainerExecution
                          })
                      }
                  p = Tl(v, b.isGtmEvent)
              } else
                  p = void 0;
              var B = p;
              if (B) {
                  Jj(m, c);
                  for (var D = [], I = 0; I < B.length; I++) {
                      var H = B[I]
                        , E = J(b);
                      if (-1 !== Nr.indexOf(H.prefix)) {
                          var L = J(d)
                            , M = E.eventMetadata || {};
                          M.hasOwnProperty("is_external_event") || (M.is_external_event = !E.fromContainerExecution);
                          E.eventMetadata = M;
                          delete L[N.g.mc];
                          zr(c, L, H.id, E)
                      }
                      D.push(H.id)
                  }
                  g.eventModel = g.eventModel || {};
                  0 < B.length ? g.eventModel[N.g.Kb] = D.join() : delete g.eventModel[N.g.Kb];
                  Or || K(43);
                  void 0 === b.noGtmEvent && b.eventMetadata && b.eventMetadata.syn_or_mod && (b.noGtmEvent = !0);
                  return b.noGtmEvent ? void 0 : g
              }
          }
      },
      get: function(a, b) {
          K(53);
          if (4 === a.length && h(a[1]) && h(a[2]) && sa(a[3])) {
              var c = Rl(a[1], b.isGtmEvent)
                , d = String(a[2])
                , e = a[3];
              if (c) {
                  Or || K(43);
                  var f = Vr();
                  if (!va(ii(), function(l) {
                      return c.W === l
                  }))
                      op(c.W, f, {
                          source: 4,
                          fromContainerExecution: b.fromContainerExecution
                      });
                  else if (-1 !== Nr.indexOf(c.prefix)) {
                      Qr(a, b);
                      var g = {};
                      ih(J((g[N.g.La] = d,
                      g[N.g.ab] = e,
                      g)));
                      Ar(d, function(l) {
                          F(function() {
                              return e(l)
                          })
                      }, c.id, b)
                  }
              }
          }
      },
      js: function(a, b) {
          if (2 == a.length && a[1].getTime) {
              Or = !0;
              var c = Qr(a, b)
                , d = c.eventId
                , e = c.priorityId
                , f = {};
              return f.event = "gtm.js",
              f["gtm.start"] = a[1].getTime(),
              f["gtm.uniqueEventId"] = d,
              f["gtm.priorityId"] = e,
              f
          }
      },
      policy: function() {},
      set: function(a, b) {
          var c;
          2 == a.length && G(a[1]) ? c = J(a[1]) : 3 == a.length && h(a[1]) && (c = {},
          G(a[2]) || ua(a[2]) ? c[a[1]] = J(a[2]) : c[a[1]] = a[2]);
          if (c) {
              var d = Qr(a, b)
                , e = d.eventId
                , f = d.priorityId;
              J(c);
              var g = J(c);
              yr.push("set", [g], void 0, b);
              c["gtm.uniqueEventId"] = e;
              f && (c["gtm.priorityId"] = f);
              R(30) && delete c.event;
              b.overwriteModelFields = !0;
              return c
          }
      }
  }
    , Xr = {
      policy: !0
  };
  var Yr = function(a) {
      var b = z[ne.da].hide;
      if (b && void 0 !== b[a] && b.end) {
          b[a] = !1;
          var c = !0, d;
          for (d in b)
              if (b.hasOwnProperty(d) && !0 === b[d]) {
                  c = !1;
                  break
              }
          c && (b.end(),
          b.end = null)
      }
  }
    , Zr = function(a) {
      var b = z[ne.da]
        , c = b && b.hide;
      c && c.end && (c[a] = !0)
  };
  var $r = !1
    , as = [];
  function bs() {
      if (!$r) {
          $r = !0;
          for (var a = 0; a < as.length; a++)
              F(as[a])
      }
  }
  var cs = function(a) {
      $r ? F(a) : as.push(a)
  };
  var ts = function(a) {
      if (ss(a))
          return a;
      this.h = a
  };
  ts.prototype.getUntrustedMessageValue = function() {
      return this.h
  }
  ;
  var ss = function(a) {
      return !a || "object" !== ac(a) || G(a) ? !1 : "getUntrustedMessageValue"in a
  };
  ts.prototype.getUntrustedMessageValue = ts.prototype.getUntrustedMessageValue;
  var us = 0
    , vs = {}
    , ws = []
    , xs = []
    , ys = !1
    , zs = !1;
  function As(a, b) {
      return a.messageContext.eventId - b.messageContext.eventId || a.messageContext.priorityId - b.messageContext.priorityId
  }
  var Bs = function(a) {
      return z[ne.da].push(a)
  }
    , Cs = function(a, b) {
      var c = oe[ne.da]
        , d = c ? c.subscribers : 1
        , e = 0
        , f = !1
        , g = void 0;
      b && (g = z.setTimeout(function() {
          f || (f = !0,
          a());
          g = void 0
      }, b));
      return function() {
          ++e === d && (g && (z.clearTimeout(g),
          g = void 0),
          f || (a(),
          f = !0))
      }
  };
  function Ds(a, b) {
      var c = a._clear || b.overwriteModelFields;
      k(a, function(e, f) {
          "_clear" !== e && (c && Se(e),
          Se(e, f))
      });
      Ee || (Ee = a["gtm.start"]);
      var d = a["gtm.uniqueEventId"];
      if (!a.event)
          return !1;
      "number" !== typeof d && (d = Je(),
      a["gtm.uniqueEventId"] = d,
      Se("gtm.uniqueEventId", d));
      return xr(a)
  }
  function Es(a) {
      if (null == a || "object" !== typeof a)
          return !1;
      if (a.event)
          return !0;
      if (Aa(a)) {
          var b = a[0];
          if ("config" === b || "event" === b || "js" === b || "get" === b)
              return !0
      }
      return !1
  }
  function Fs() {
      var a;
      if (xs.length)
          a = xs.shift();
      else if (ws.length)
          a = ws.shift();
      else
          return;
      var b;
      var c = a;
      if (ys || !Es(c.message))
          b = c;
      else {
          ys = !0;
          var d = c.message["gtm.uniqueEventId"];
          "number" !== typeof d && (d = c.message["gtm.uniqueEventId"] = Je());
          var e = {}
            , f = {
              message: (e.event = "gtm.init_consent",
              e["gtm.uniqueEventId"] = d - 2,
              e),
              messageContext: {
                  eventId: d - 2
              }
          }
            , g = {}
            , l = {
              message: (g.event = "gtm.init",
              g["gtm.uniqueEventId"] = d - 1,
              g),
              messageContext: {
                  eventId: d - 1
              }
          };
          ws.unshift(l, c);
          if (mj && T.C) {
              var m, n = ji(ni());
              m = n && n.context;
              var p, q = zf(z.location.href);
              p = q.hostname + q.pathname;
              var r = m && m.fromContainerExecution
                , t = m && m.source
                , u = T.C
                , v = T.Ua
                , w = T.Ce;
              xj || (xj = p);
              wj.push(u + ";" + v + ";" + (r ? 1 : 0) + ";" + (t || 0) + ";" + (w ? 1 : 0))
          }
          b = f
      }
      return b
  }
  function Gs() {
      for (var a = !1, b; !zs && (b = Fs()); ) {
          zs = !0;
          delete Me.eventModel;
          Oe();
          var c = b
            , d = c.message
            , e = c.messageContext;
          if (null == d)
              zs = !1;
          else {
              if (e.fromContainerExecution)
                  for (var f = ["gtm.allowlist", "gtm.blocklist", "gtm.whitelist", "gtm.blacklist", "tagTypeBlacklist"], g = 0; g < f.length; g++) {
                      var l = f[g]
                        , m = Pe(l, 1);
                      if (ua(m) || G(m))
                          m = J(m);
                      Ne[l] = m
                  }
              try {
                  if (sa(d))
                      try {
                          d.call(Qe)
                      } catch (D) {}
                  else if (ua(d)) {
                      var n = d;
                      if (h(n[0])) {
                          var p = n[0].split(".")
                            , q = p.pop()
                            , r = n.slice(1)
                            , t = Pe(p.join("."), 2);
                          if (null != t)
                              try {
                                  t[q].apply(t, r)
                              } catch (D) {}
                      }
                  } else {
                      var u = void 0
                        , v = !1;
                      if (Aa(d)) {
                          a: {
                              if (d.length && h(d[0])) {
                                  var w = Wr[d[0]];
                                  if (w && (!e.fromContainerExecution || !Xr[d[0]])) {
                                      u = w(d, e);
                                      break a
                                  }
                              }
                              u = void 0
                          }
                          (v = u && "set" === d[0] && !!u.event) && K(101)
                      } else
                          u = d;
                      if (u) {
                          var x = Ds(u, e);
                          a = x || a;
                          v && x && K(113)
                      }
                  }
              } finally {
                  e.fromContainerExecution && Oe(!0);
                  var y = d["gtm.uniqueEventId"];
                  if ("number" === typeof y) {
                      for (var A = vs[String(y)] || [], B = 0; B < A.length; B++)
                          xs.push(Hs(A[B]));
                      A.length && xs.sort(As);
                      delete vs[String(y)];
                      y > us && (us = y)
                  }
                  zs = !1
              }
          }
      }
      return !a
  }
  function Is() {
      if (R(70)) {
          var a = ho(bo.F.df, T.C);
          io(a);
          if (Js()) {
              var b = ho(bo.F.Eg, T.C);
              if (io(b)) {
                  var c = ho(bo.F.ff, T.C);
                  jo(b, c)
              }
          }
      }
      var d = Gs();
      try {
          Yr(T.C)
      } catch (e) {}
      return d
  }
  function cr(a) {
      if (us < a.notBeforeEventId) {
          var b = String(a.notBeforeEventId);
          vs[b] = vs[b] || [];
          vs[b].push(a)
      } else
          xs.push(Hs(a)),
          xs.sort(As),
          F(function() {
              zs || Gs()
          })
  }
  function Hs(a) {
      return {
          message: a.message,
          messageContext: a.messageContext
      }
  }
  var Ks = function() {
      function a(g) {
          var l = {};
          if (ss(g)) {
              var m = g;
              g = ss(m) ? m.getUntrustedMessageValue() : void 0;
              l.fromContainerExecution = !0
          }
          return {
              message: g,
              messageContext: l
          }
      }
      var b = Gb(ne.da, [])
        , c = oe[ne.da] = oe[ne.da] || {};
      !0 === c.pruned && K(83);
      vs = ar().get();
      dr();
      Ip(function() {
          if (!c.gtmDom) {
              c.gtmDom = !0;
              var g = {};
              b.push((g.event = "gtm.dom",
              g))
          }
      });
      cs(function() {
          if (!c.gtmLoad) {
              c.gtmLoad = !0;
              var g = {};
              b.push((g.event = "gtm.load",
              g))
          }
      });
      c.subscribers = (c.subscribers || 0) + 1;
      var d = b.push;
      b.push = function() {
          var g;
          if (0 < oe.SANDBOXED_JS_SEMAPHORE) {
              g = [];
              for (var l = 0; l < arguments.length; l++)
                  g[l] = new ts(arguments[l])
          } else
              g = [].slice.call(arguments, 0);
          var m = g.map(function(r) {
              return a(r)
          });
          ws.push.apply(ws, m);
          var n = d.apply(b, g)
            , p = Math.max(100, Number("1000") || 300);
          if (this.length > p)
              for (K(4),
              c.pruned = !0; this.length > p; )
                  this.shift();
          var q = "boolean" !== typeof n || n;
          return Gs() && q
      }
      ;
      var e = b.slice(0).map(function(g) {
          return a(g)
      });
      ws.push.apply(ws, e);
      if (Js()) {
          if (R(70)) {
              var f = ho(bo.F.ff, T.C);
              io(f)
          }
          F(Is)
      }
  }
    , Js = function() {
      var a = !0;
      return a
  };
  function Ls(a) {
      if (null == a || 0 === a.length)
          return !1;
      var b = Number(a)
        , c = Ha();
      return b < c + 3E5 && b > c - 9E5
  }
  function Ms(a) {
      return a && 0 === a.indexOf("pending:") ? Ls(a.substr(8)) : !1
  }
  ;var Mc = {};
  Mc.Be = new String("undefined");
  var ht = function(a) {
      this.h = function(b) {
          for (var c = [], d = 0; d < a.length; d++)
              c.push(a[d] === Mc.Be ? b : a[d]);
          return c.join("")
      }
  };
  ht.prototype.toString = function() {
      return this.h("undefined")
  }
  ;
  ht.prototype.valueOf = ht.prototype.toString;
  Mc.Sj = ht;
  Mc.Jf = {};
  Mc.fk = function(a) {
      return new ht(a)
  }
  ;
  var it = {};
  Mc.ql = function(a, b) {
      var c = Je();
      it[c] = [a, b];
      return c
  }
  ;
  Mc.Zh = function(a) {
      var b = a ? 0 : 1;
      return function(c) {
          var d = it[c];
          if (d && "function" === typeof d[b])
              d[b]();
          it[c] = void 0
      }
  }
  ;
  Mc.Ik = function(a) {
      for (var b = !1, c = !1, d = 2; d < a.length; d++)
          b = b || 8 === a[d],
          c = c || 16 === a[d];
      return b && c
  }
  ;
  Mc.il = function(a) {
      if (a === Mc.Be)
          return a;
      var b = Je();
      Mc.Jf[b] = a;
      return 'google_tag_manager["' + T.C + '"].macro(' + b + ")"
  }
  ;
  Mc.Vk = function(a, b, c) {
      a instanceof Mc.Sj && (a = a.h(Mc.ql(b, c)),
      b = ra);
      return {
          Ck: a,
          K: b
      }
  }
  ;
  var It = z.clearTimeout
    , Jt = z.setTimeout
    , U = function(a, b, c, d) {
      if (ci()) {
          b && F(b)
      } else
          return Lb(a, b, c, d)
  }
    , Kt = function() {
      return new Date
  }
    , Lt = function() {
      return z.location.href
  }
    , Mt = function(a) {
      return xf(zf(a), "fragment")
  }
    , Nt = function(a) {
      return yf(zf(a))
  }
    , Ot = function(a, b) {
      return Pe(a, b || 2)
  }
    , Pt = function(a, b, c) {
      var d;
      b ? (a.eventCallback = b,
      c && (a.eventTimeout = c),
      d = Bs(a)) : d = Bs(a);
      return d
  }
    , Qt = function(a, b) {
      z[a] = b
  }
    , W = function(a, b, c) {
      b && (void 0 === z[a] || c && !z[a]) && (z[a] = b);
      return z[a]
  }
    , Rt = function(a, b, c) {
      return Kh(a, b, void 0 === c ? !0 : !!c)
  }
    , St = function(a, b, c) {
      return 0 === Th(a, b, c)
  }
    , Tt = function(a, b) {
      if (ci()) {
          b && F(b)
      } else
          Nb(a, b)
  }
    , Ut = function(a) {
      return !!nt(a, "init", !1)
  }
    , Vt = function(a) {
      lt(a, "init", !0)
  }
    , Wt = function(a, b, c) {
      cc(a) || Pq(c, b, a)
  };

  var Xt = Mc.Vk;
  function tu(a, b) {
      function c(g) {
          var l = zf(g)
            , m = xf(l, "protocol")
            , n = xf(l, "host", !0)
            , p = xf(l, "port")
            , q = xf(l, "path").toLowerCase().replace(/\/$/, "");
          if (void 0 === m || "http" === m && "80" === p || "https" === m && "443" === p)
              m = "web",
              p = "default";
          return [m, n, p, q]
      }
      for (var d = c(String(a)), e = c(String(b)), f = 0; f < d.length; f++)
          if (d[f] !== e[f])
              return !1;
      return !0
  }
  function uu(a) {
      return vu(a) ? 1 : 0
  }
  function vu(a) {
      var b = a.arg0
        , c = a.arg1;
      if (a.any_of && Array.isArray(c)) {
          for (var d = 0; d < c.length; d++) {
              var e = J(a, {});
              J({
                  arg1: c[d],
                  any_of: void 0
              }, e);
              if (uu(e))
                  return !0
          }
          return !1
      }
      switch (a["function"]) {
      case "_cn":
          return 0 <= String(b).indexOf(String(c));
      case "_css":
          var f;
          a: {
              if (b)
                  try {
                      for (var g = 0; g < kd.length; g++) {
                          var l = kd[g];
                          if (b[l]) {
                              f = b[l](c);
                              break a
                          }
                      }
                  } catch (m) {}
              f = !1
          }
          return f;
      case "_ew":
          return ld(b, c);
      case "_eq":
          return String(b) === String(c);
      case "_ge":
          return Number(b) >= Number(c);
      case "_gt":
          return Number(b) > Number(c);
      case "_lc":
          return 0 <= String(b).split(",").indexOf(String(c));
      case "_le":
          return Number(b) <= Number(c);
      case "_lt":
          return Number(b) < Number(c);
      case "_re":
          return nd(b, c, a.ignore_case);
      case "_sw":
          return 0 === String(b).indexOf(String(c));
      case "_um":
          return tu(b, c)
      }
      return !1
  }
  ;function wu() {
      function a(c, d) {
          var e = bb(d);
          e && b.push(c + "=" + e)
      }
      var b = [];
      a("&u", "GTM");
      a("&ut", "TAGGING");
      a("&h", "HEALTH");
      return b.join("")
  }
  ;$e();
  function Su() {
      return z.gaGlobal = z.gaGlobal || {}
  }
  var Tu = function() {
      var a = Su();
      a.hid = a.hid || wa();
      return a.hid
  }
    , Uu = function(a, b) {
      var c = Su();
      if (void 0 == c.vid || b && !c.from_cookie)
          c.vid = a,
          c.from_cookie = b
  };
  var qv = function() {
      var a = !0;
      ej(7) && ej(9) && ej(10) || (a = !1);
      return a
  }
    , rv = function() {
      var a = !0;
      ej(3) && ej(4) || (a = !1);
      return a
  };
  var Sv = window
    , Tv = document
    , Uv = function(a) {
      var b = Sv._gaUserPrefs;
      if (b && b.ioo && b.ioo() || Tv.documentElement.hasAttribute("data-google-analytics-opt-out") || a && !0 === Sv["ga-disable-" + a])
          return !0;
      try {
          var c = Sv.external;
          if (c && c._gaUserPrefs && "oo" == c._gaUserPrefs)
              return !0
      } catch (f) {}
      for (var d = Eh("AMP_TOKEN", String(Tv.cookie), !0), e = 0; e < d.length; e++)
          if ("$OPT_OUT" == d[e])
              return !0;
      return Tv.getElementById("__gaOptOutExtension") ? !0 : !1
  };
  function $v(a) {
      k(a, function(c) {
          "_" === c.charAt(0) && delete a[c]
      });
      var b = a[N.g.Na] || {};
      k(b, function(c) {
          "_" === c.charAt(0) && delete b[c]
      })
  }
  ;var iw = function(a, b) {};
  function hw(a, b) {
      var c = function() {};
      return c
  }
  function jw(a, b, c) {}
  ;var bx = function(a, b) {
      if (!b.isGtmEvent) {
          var c = S(b, N.g.La)
            , d = S(b, N.g.ab)
            , e = S(b, c);
          if (void 0 === e) {
              var f = void 0;
              Zw.hasOwnProperty(c) ? f = Zw[c] : $w.hasOwnProperty(c) && (f = $w[c]);
              1 === f && (f = ax(c));
              h(f) ? Vp()(function() {
                  var g = Vp().getByName(a).get(f);
                  d(g)
              }) : d(void 0)
          } else
              d(e)
      }
  }
    , cx = function(a, b) {
      var c = a[N.g.Hb]
        , d = b + "."
        , e = a[N.g.N] || ""
        , f = void 0 === c ? !!a.use_anchor : "fragment" === c
        , g = !!a[N.g.wb];
      e = String(e).replace(/\s+/g, "").split(",");
      var l = Vp();
      l(d + "require", "linker");
      l(d + "linker:autoLink", e, f, g)
  }
    , gx = function(a, b, c) {
      if (Ug() && (!c.isGtmEvent || !dx[a])) {
          var d = !Sg(N.g.M)
            , e = function(f) {
              var g, l, m = Vp(), n = ex(b, "", c), p, q = n.createOnlyFields._useUp;
              if (c.isGtmEvent || fx(b, n.createOnlyFields)) {
                  c.isGtmEvent && (g = "gtm" + Je(),
                  l = n.createOnlyFields,
                  n.gtmTrackerName && (l.name = g));
                  m(function() {
                      var t = m.getByName(b);
                      t && (p = t.get("clientId"));
                      c.isGtmEvent || m.remove(b)
                  });
                  m("create", a, c.isGtmEvent ? l : n.createOnlyFields);
                  d && Sg(N.g.M) && (d = !1,
                  m(function() {
                      var t = Vp().getByName(c.isGtmEvent ? g : b);
                      !t || t.get("clientId") == p && q || (c.isGtmEvent ? (n.fieldsToSet["&gcu"] = "1",
                      n.fieldsToSet["&sst.gcut"] = ke[f]) : (n.fieldsToSend["&gcu"] = "1",
                      n.fieldsToSend["&sst.gcut"] = ke[f]),
                      t.set(n.fieldsToSet),
                      c.isGtmEvent ? t.send("pageview") : t.send("pageview", n.fieldsToSend))
                  }));
                  c.isGtmEvent && m(function() {
                      m.remove(g)
                  })
              }
          };
          Bh(function() {
              return e(N.g.M)
          }, N.g.M);
          Bh(function() {
              return e(N.g.D)
          }, N.g.D);
          c.isGtmEvent && (dx[a] = !0)
      }
  }
    , hx = function(a, b) {
      jp() && b && (a[N.g.Fb] = b)
  }
    , qx = function(a, b, c) {
      function d() {
          var E = S(c, N.g.jc);
          l(function() {
              if (!c.isGtmEvent && G(E)) {
                  var L = u.fieldsToSend, M = m().getByName(n), Y;
                  for (Y in E)
                      if (E.hasOwnProperty(Y) && /^(dimension|metric)\d+$/.test(Y) && void 0 != E[Y]) {
                          var V = M.get(ax(E[Y]));
                          ix(L, Y, V)
                      }
              }
          })
      }
      function e() {
          if (u.displayfeatures) {
              var E = "_dc_gtm_" + f.replace(/[^A-Za-z0-9-]/g, "");
              p("require", "displayfeatures", void 0, {
                  cookieName: E
              })
          }
      }
      var f = a
        , g = "https://www.google-analytics.com/analytics.js"
        , l = c.isGtmEvent ? Xp(S(c, "gaFunctionName")) : Xp();
      if (sa(l)) {
          var m = Vp, n;
          c.isGtmEvent ? n = S(c, "name") || S(c, "gtmTrackerName") : n = "gtag_" + f.split("-").join("_");
          var p = function(E) {
              var L = [].slice.call(arguments, 0);
              L[0] = n ? n + "." + L[0] : "" + L[0];
              l.apply(window, L)
          }
            , q = function(E) {
              var L = function(ha, ca) {
                  for (var aa = 0; ca && aa < ca.length; aa++)
                      p(ha, ca[aa])
              }
                , M = c.isGtmEvent
                , Y = M ? jx(u) : kx(b, c);
              if (Y) {
                  var V = {};
                  hx(V, E);
                  p("require", "ec", "ec.js", V);
                  M && Y.Rf && p("set", "&cu", Y.Rf);
                  var Q = Y.action;
                  if (M || "impressions" === Q)
                      if (L("ec:addImpression", Y.ii),
                      !M)
                          return;
                  if ("promo_click" === Q || "promo_view" === Q || M && Y.Id) {
                      var P = Y.Id;
                      L("ec:addPromo", P);
                      if (P && 0 < P.length && "promo_click" === Q) {
                          M ? p("ec:setAction", Q, Y.Qa) : p("ec:setAction", Q);
                          return
                      }
                      if (!M)
                          return
                  }
                  "promo_view" !== Q && "impressions" !== Q && (L("ec:addProduct", Y.Qb),
                  p("ec:setAction", Q, Y.Qa))
              }
          }
            , r = function(E) {
              if (E) {
                  var L = {};
                  if (G(E))
                      for (var M in lx)
                          lx.hasOwnProperty(M) && mx(lx[M], M, E[M], L);
                  hx(L, x);
                  p("require", "linkid", L)
              }
          }
            , t = function() {
              if (ci()) {} else {
                  var E = S(c, N.g.uj);
                  E && (p("require", E, {
                      dataLayer: ne.da
                  }),
                  p("require", "render"))
              }
          }
            , u = ex(n, b, c)
            , v = function(E, L, M) {
              M && (L = "" + L);
              u.fieldsToSend[E] = L
          };
          !c.isGtmEvent && fx(n, u.createOnlyFields) && (l(function() {
              m() && m().remove(n)
          }),
          nx[n] = !1);
          l("create", f, u.createOnlyFields);
          if (u.createOnlyFields[N.g.Fb] && !c.isGtmEvent) {
              var w = xe || ze ? ip(u.createOnlyFields[N.g.Fb], "/analytics.js") : void 0;
              w && (g = w)
          }
          var x = c.isGtmEvent ? u.fieldsToSet[N.g.Fb] : u.createOnlyFields[N.g.Fb];
          if (x) {
              var y = c.isGtmEvent ? u.fieldsToSet[N.g.oe] : u.createOnlyFields[N.g.oe];
              y && !nx[n] && (nx[n] = !0,
              l(Fq(n, y)))
          }
          c.isGtmEvent ? u.enableRecaptcha && p("require", "recaptcha", "recaptcha.js") : (d(),
          r(u.linkAttribution));
          var A = u[N.g.wa];
          A && A[N.g.N] && cx(A, n);
          p("set", u.fieldsToSet);
          if (c.isGtmEvent) {
              if (u.enableLinkId) {
                  var B = {};
                  hx(B, x);
                  p("require", "linkid", "linkid.js", B)
              }
              Ug() && gx(f, n, c)
          }
          if (b === N.g.fc)
              if (c.isGtmEvent) {
                  e();
                  if (u.remarketingLists) {
                      var D = "_dc_gtm_" + f.replace(/[^A-Za-z0-9-]/g, "");
                      p("require", "adfeatures", {
                          cookieName: D
                      })
                  }
                  q(x);
                  p("send", "pageview");
                  u.createOnlyFields._useUp && qq(n + ".")
              } else
                  t(),
                  p("send", "pageview", u.fieldsToSend);
          else
              b === N.g.ja ? (t(),
              em(f, c),
              S(c, N.g.fb) && (Gl(["aw", "dc"]),
              qq(n + ".")),
              0 != u.sendPageView && p("send", "pageview", u.fieldsToSend),
              gx(f, n, c)) : b === N.g.Ea ? bx(n, c) : "screen_view" === b ? p("send", "screenview", u.fieldsToSend) : "timing_complete" === b ? (u.fieldsToSend.hitType = "timing",
              v("timingCategory", u.eventCategory, !0),
              c.isGtmEvent ? v("timingVar", u.timingVar, !0) : v("timingVar", u.name, !0),
              v("timingValue", Ba(u.value)),
              void 0 !== u.eventLabel && v("timingLabel", u.eventLabel, !0),
              p("send", u.fieldsToSend)) : "exception" === b ? p("send", "exception", u.fieldsToSend) : "" === b && c.isGtmEvent || ("track_social" === b && c.isGtmEvent ? (u.fieldsToSend.hitType = "social",
              v("socialNetwork", u.socialNetwork, !0),
              v("socialAction", u.socialAction, !0),
              v("socialTarget", u.socialTarget, !0)) : ((c.isGtmEvent || ox[b]) && q(x),
              c.isGtmEvent && e(),
              u.fieldsToSend.hitType = "event",
              v("eventCategory", u.eventCategory, !0),
              v("eventAction", u.eventAction || b, !0),
              void 0 !== u.eventLabel && v("eventLabel", u.eventLabel, !0),
              void 0 !== u.value && v("eventValue", Ba(u.value))),
              p("send", u.fieldsToSend));
          if (!px && !c.isGtmEvent) {
              px = !0;
              var I = function() {
                  c.O()
              }
                , H = function() {
                  m().loaded || I()
              };
              ci() ? F(H) : Lb(g, H, I)
          }
      } else
          F(c.O)
  }
    , rx = function(a, b, c, d) {
      Ch(function() {
          qx(a, b, d)
      }, [N.g.M, N.g.D])
  }
    , tx = function(a) {
      function b(e) {
          function f(l, m) {
              for (var n = 0; n < m.length; n++) {
                  var p = m[n];
                  if (e[p]) {
                      g[l] = e[p];
                      break
                  }
              }
          }
          var g = J(e);
          f("id", ["id", "item_id", "promotion_id"]);
          f("name", ["name", "item_name", "promotion_name"]);
          f("brand", ["brand", "item_brand"]);
          f("variant", ["variant", "item_variant"]);
          f("list", ["list_name", "item_list_name"]);
          f("position", ["list_position", "creative_slot", "index"]);
          (function() {
              if (e.category)
                  g.category = e.category;
              else {
                  for (var l = "", m = 0; m < sx.length; m++)
                      void 0 !== e[sx[m]] && (l && (l += "/"),
                      l += e[sx[m]]);
                  l && (g.category = l)
              }
          }
          )();
          f("listPosition", ["list_position"]);
          f("creative", ["creative_name"]);
          f("list", ["list_name"]);
          f("position", ["list_position", "creative_slot"]);
          return g
      }
      for (var c = [], d = 0; a && d < a.length; d++)
          a[d] && G(a[d]) && c.push(b(a[d]));
      return c.length ? c : void 0
  }
    , ux = function(a) {
      return Sg(a)
  }
    , vx = !1;
  var px, nx = {}, dx = {}, wx = {}, xx = Object.freeze((wx.page_hostname = 1,
  wx[N.g.T] = 1,
  wx[N.g.rb] = 1,
  wx[N.g.Ja] = 1,
  wx[N.g.za] = 1,
  wx[N.g.Ka] = 1,
  wx[N.g.ic] = 1,
  wx[N.g.Tc] = 1,
  wx[N.g.Ga] = 1,
  wx[N.g.Za] = 1,
  wx[N.g.fa] = 1,
  wx[N.g.Ib] = 1,
  wx[N.g.Aa] = 1,
  wx[N.g.xb] = 1,
  wx)), yx = {}, Zw = Object.freeze((yx.client_storage = "storage",
  yx.sample_rate = 1,
  yx.site_speed_sample_rate = 1,
  yx.store_gac = 1,
  yx.use_amp_client_id = 1,
  yx[N.g.Xa] = 1,
  yx[N.g.ra] = "storeGac",
  yx[N.g.Ja] = 1,
  yx[N.g.za] = 1,
  yx[N.g.Ka] = 1,
  yx[N.g.ic] = 1,
  yx[N.g.Tc] = 1,
  yx[N.g.Za] = 1,
  yx)), zx = {}, Ax = Object.freeze((zx._cs = 1,
  zx._useUp = 1,
  zx.allowAnchor = 1,
  zx.allowLinker = 1,
  zx.alwaysSendReferrer = 1,
  zx.clientId = 1,
  zx.cookieDomain = 1,
  zx.cookieExpires = 1,
  zx.cookieFlags = 1,
  zx.cookieName = 1,
  zx.cookiePath = 1,
  zx.cookieUpdate = 1,
  zx.legacyCookieDomain = 1,
  zx.legacyHistoryImport = 1,
  zx.name = 1,
  zx.sampleRate = 1,
  zx.siteSpeedSampleRate = 1,
  zx.storage = 1,
  zx.storeGac = 1,
  zx.useAmpClientId = 1,
  zx._cd2l = 1,
  zx)), Bx = Object.freeze({
      anonymize_ip: 1
  }), Cx = {}, $w = Object.freeze((Cx.campaign = {
      content: "campaignContent",
      id: "campaignId",
      medium: "campaignMedium",
      name: "campaignName",
      source: "campaignSource",
      term: "campaignKeyword"
  },
  Cx.app_id = 1,
  Cx.app_installer_id = 1,
  Cx.app_name = 1,
  Cx.app_version = 1,
  Cx.description = "exDescription",
  Cx.fatal = "exFatal",
  Cx.language = 1,
  Cx.page_hostname = "hostname",
  Cx.transport_type = "transport",
  Cx[N.g.oa] = "currencyCode",
  Cx[N.g.nh] = 1,
  Cx[N.g.fa] = "location",
  Cx[N.g.Ib] = "page",
  Cx[N.g.Aa] = "referrer",
  Cx[N.g.xb] = "title",
  Cx[N.g.Af] = 1,
  Cx[N.g.xa] = 1,
  Cx)), Dx = {}, Ex = Object.freeze((Dx.content_id = 1,
  Dx.event_action = 1,
  Dx.event_category = 1,
  Dx.event_label = 1,
  Dx.link_attribution = 1,
  Dx.name = 1,
  Dx[N.g.wa] = 1,
  Dx[N.g.mh] = 1,
  Dx[N.g.Ma] = 1,
  Dx[N.g.Z] = 1,
  Dx)), Fx = Object.freeze({
      displayfeatures: 1,
      enableLinkId: 1,
      enableRecaptcha: 1,
      eventAction: 1,
      eventCategory: 1,
      eventLabel: 1,
      gaFunctionName: 1,
      gtmEcommerceData: 1,
      gtmTrackerName: 1,
      linker: 1,
      remarketingLists: 1,
      socialAction: 1,
      socialNetwork: 1,
      socialTarget: 1,
      timingVar: 1,
      value: 1
  }), sx = Object.freeze(["item_category", "item_category2", "item_category3", "item_category4", "item_category5"]), Gx = {}, lx = Object.freeze((Gx.levels = 1,
  Gx[N.g.za] = "duration",
  Gx[N.g.ic] = 1,
  Gx)), Hx = {}, Ix = Object.freeze((Hx.anonymize_ip = 1,
  Hx.fatal = 1,
  Hx.send_page_view = 1,
  Hx.store_gac = 1,
  Hx.use_amp_client_id = 1,
  Hx[N.g.ra] = 1,
  Hx[N.g.nh] = 1,
  Hx)), mx = function(a, b, c, d) {
      if (void 0 !== c)
          if (Ix[b] && (c = Da(c)),
          "anonymize_ip" !== b || c || (c = void 0),
          1 === a)
              d[ax(b)] = c;
          else if (h(a))
              d[a] = c;
          else
              for (var e in a)
                  a.hasOwnProperty(e) && void 0 !== c[e] && (d[a[e]] = c[e])
  }, ax = function(a) {
      return a && h(a) ? a.replace(/(_[a-z])/g, function(b) {
          return b[1].toUpperCase()
      }) : a
  }, Jx = {}, ox = Object.freeze((Jx.checkout_progress = 1,
  Jx.select_content = 1,
  Jx.set_checkout_option = 1,
  Jx[N.g.Yb] = 1,
  Jx[N.g.Zb] = 1,
  Jx[N.g.Cb] = 1,
  Jx[N.g.ac] = 1,
  Jx[N.g.Va] = 1,
  Jx[N.g.pb] = 1,
  Jx[N.g.Wa] = 1,
  Jx[N.g.Ca] = 1,
  Jx[N.g.bc] = 1,
  Jx[N.g.Da] = 1,
  Jx)), Kx = {}, Lx = Object.freeze((Kx.checkout_progress = 1,
  Kx.set_checkout_option = 1,
  Kx[N.g.Kg] = 1,
  Kx[N.g.Lg] = 1,
  Kx[N.g.Yb] = 1,
  Kx[N.g.Zb] = 1,
  Kx[N.g.Mg] = 1,
  Kx[N.g.Cb] = 1,
  Kx[N.g.Ca] = 1,
  Kx[N.g.bc] = 1,
  Kx[N.g.Ng] = 1,
  Kx)), Mx = {}, Nx = Object.freeze((Mx.generate_lead = 1,
  Mx.login = 1,
  Mx.search = 1,
  Mx.select_content = 1,
  Mx.share = 1,
  Mx.sign_up = 1,
  Mx.view_search_results = 1,
  Mx[N.g.ac] = 1,
  Mx[N.g.Va] = 1,
  Mx[N.g.pb] = 1,
  Mx[N.g.Wa] = 1,
  Mx[N.g.Da] = 1,
  Mx)), Ox = function(a) {
      var b = "general";
      Lx[a] ? b = "ecommerce" : Nx[a] ? b = "engagement" : "exception" === a && (b = "error");
      return b
  }, Px = {}, Qx = Object.freeze((Px.view_search_results = 1,
  Px[N.g.Va] = 1,
  Px[N.g.Wa] = 1,
  Px[N.g.Da] = 1,
  Px)), ix = function(a, b, c) {
      a.hasOwnProperty(b) || (a[b] = c)
  }, Rx = function(a) {
      if (ua(a)) {
          for (var b = [], c = 0; c < a.length; c++) {
              var d = a[c];
              if (void 0 != d) {
                  var e = d.id
                    , f = d.variant;
                  void 0 != e && void 0 != f && b.push(String(e) + "." + String(f))
              }
          }
          return 0 < b.length ? b.join("!") : void 0
      }
  }, ex = function(a, b, c) {
      var d = function(M) {
          return S(c, M)
      }
        , e = {}
        , f = {}
        , g = {}
        , l = {}
        , m = Rx(d(N.g.sj));
      !c.isGtmEvent && m && ix(f, "exp", m);
      g["&gtm"] = ri(!0);
      c.isGtmEvent || (g._no_slc = !0);
      Ug() && (l._cs = ux);
      var n = d(N.g.jc);
      if (!c.isGtmEvent && G(n))
          for (var p in n)
              if (n.hasOwnProperty(p) && /^(dimension|metric)\d+$/.test(p) && void 0 != n[p]) {
                  var q = d(String(n[p]));
                  void 0 !== q && ix(f, p, q)
              }
      for (var r = !c.isGtmEvent, t = Dm(c), u = 0; u < t.length; ++u) {
          var v = t[u];
          if (c.isGtmEvent) {
              var w = d(v);
              Fx.hasOwnProperty(v) ? e[v] = w : Ax.hasOwnProperty(v) ? l[v] = w : g[v] = w
          } else {
              var x = void 0;
              x = v !== N.g.V ? d(v) : Em(c, v);
              if (Ex.hasOwnProperty(v))
                  mx(Ex[v], v, x, e);
              else if (Bx.hasOwnProperty(v))
                  mx(Bx[v], v, x, g);
              else if ($w.hasOwnProperty(v))
                  mx($w[v], v, x, f);
              else if (Zw.hasOwnProperty(v))
                  mx(Zw[v], v, x, l);
              else if (/^(dimension|metric|content_group)\d+$/.test(v))
                  mx(1, v, x, f);
              else if (v === N.g.V) {
                  if (!vx) {
                      var y = Qa(x);
                      y && (f["&did"] = y)
                  }
                  var A = void 0
                    , B = void 0;
                  b === N.g.ja ? A = Qa(Em(c, v), ".") : (A = Qa(Em(c, v, 1), "."),
                  B = Qa(Em(c, v, 2), "."));
                  A && (f["&gdid"] = A);
                  B && (f["&edid"] = B)
              } else
                  v === N.g.Ga && 0 > t.indexOf(N.g.ic) && (l.cookieName = x + "_ga");
              R(96) && xx[v] && (c.m.hasOwnProperty(v) || b === N.g.ja && c.h.hasOwnProperty(v)) && (r = !1)
          }
      }
      R(96) && r && (f["&jsscut"] = "1");
      !1 !== d(N.g.jf) && !1 !== d(N.g.rb) && qv() || (g.allowAdFeatures = !1);
      !1 !== d(N.g.T) && rv() || (g.allowAdPersonalizationSignals = !1);
      !c.isGtmEvent && d(N.g.fb) && (l._useUp = !0);
      if (c.isGtmEvent) {
          l.name = l.name || e.gtmTrackerName;
          var D = g.hitCallback;
          g.hitCallback = function() {
              sa(D) && D();
              c.K()
          }
      } else {
          ix(l, "cookieDomain", "auto");
          ix(g, "forceSSL", !0);
          ix(e, "eventCategory", Ox(b));
          Qx[b] && ix(f, "nonInteraction", !0);
          "login" === b || "sign_up" === b || "share" === b ? ix(e, "eventLabel", d(N.g.mh)) : "search" === b || "view_search_results" === b ? ix(e, "eventLabel", d(N.g.Bj)) : "select_content" === b && ix(e, "eventLabel", d(N.g.kj));
          var I = e[N.g.wa] || {}
            , H = I[N.g.oc];
          H || 0 != H && I[N.g.N] ? l.allowLinker = !0 : !1 === H && ix(l, "useAmpClientId", !1);
          f.hitCallback = c.K;
          l.name = a
      }
      Ug() && (g["&gcs"] = uh(),
      R(106) && (g["&gcd"] = yh()),
      Sg(N.g.M) || (l.storage = "none"),
      Sg(N.g.D) || (g.allowAdFeatures = !1,
      l.storeGac = !1));
      R(109) && (Ah() && (g["&dma_cps"] = zh()),
      Ye() && (g["&dma"] = "1"));
      var E = kp(c) || d(N.g.Fb)
        , L = d(N.g.oe);
      E && (c.isGtmEvent || (l[N.g.Fb] = E),
      l._cd2l = !0);
      L && !c.isGtmEvent && (l[N.g.oe] = L);
      e.fieldsToSend = f;
      e.fieldsToSet = g;
      e.createOnlyFields = l;
      return e
  }, jx = function(a) {
      var b = a.gtmEcommerceData;
      if (!b)
          return null;
      var c = {};
      b.currencyCode && (c.Rf = b.currencyCode);
      if (b.impressions) {
          c.action = "impressions";
          var d = b.impressions;
          c.ii = "impressions" === b.translateIfKeyEquals ? tx(d) : d
      }
      if (b.promoView) {
          c.action = "promo_view";
          var e = b.promoView.promotions;
          c.Id = "promoView" === b.translateIfKeyEquals ? tx(e) : e
      }
      if (b.promoClick) {
          c.action = "promo_click";
          var f = b.promoClick.promotions;
          c.Id = "promoClick" === b.translateIfKeyEquals ? tx(f) : f;
          c.Qa = b.promoClick.actionField;
          return c
      }
      for (var g in b)
          if (b.hasOwnProperty(g) && "translateIfKeyEquals" !== g && "impressions" !== g && "promoView" !== g && "promoClick" !== g && "currencyCode" !== g) {
              c.action = g;
              var l = b[g].products;
              c.Qb = "products" === b.translateIfKeyEquals ? tx(l) : l;
              c.Qa = b[g].actionField;
              break
          }
      return Object.keys(c).length ? c : null
  }, kx = function(a, b) {
      function c(u) {
          return {
              id: d(N.g.la),
              affiliation: d(N.g.Rg),
              revenue: d(N.g.Z),
              tax: d(N.g.qf),
              shipping: d(N.g.Vc),
              coupon: d(N.g.Sg),
              list: d(N.g.pf) || d(N.g.Uc) || u
          }
      }
      for (var d = function(u) {
          return S(b, u)
      }, e = d(N.g.U), f, g = 0; e && g < e.length && !(f = e[g][N.g.pf] || e[g][N.g.Uc]); g++)
          ;
      var l = d(N.g.jc);
      if (G(l))
          for (var m = 0; e && m < e.length; ++m) {
              var n = e[m], p;
              for (p in l)
                  l.hasOwnProperty(p) && /^(dimension|metric)\d+$/.test(p) && void 0 != l[p] && ix(n, p, n[l[p]])
          }
      var q = null
        , r = d(N.g.nj);
      if (a === N.g.Ca || a === N.g.bc)
          q = {
              action: a,
              Qa: c(),
              Qb: tx(e)
          };
      else if (a === N.g.Yb)
          q = {
              action: "add",
              Qa: c(),
              Qb: tx(e)
          };
      else if (a === N.g.Zb)
          q = {
              action: "remove",
              Qa: c(),
              Qb: tx(e)
          };
      else if (a === N.g.Da)
          q = {
              action: "detail",
              Qa: c(f),
              Qb: tx(e)
          };
      else if (a === N.g.Va)
          q = {
              action: "impressions",
              ii: tx(e)
          };
      else if (a === N.g.Wa)
          q = {
              action: "promo_view",
              Id: tx(r) || tx(e)
          };
      else if ("select_content" === a && r && 0 < r.length || a === N.g.pb)
          q = {
              action: "promo_click",
              Id: tx(r) || tx(e)
          };
      else if ("select_content" === a || a === N.g.ac)
          q = {
              action: "click",
              Qa: {
                  list: d(N.g.pf) || d(N.g.Uc) || f
              },
              Qb: tx(e)
          };
      else if (a === N.g.Cb || "checkout_progress" === a) {
          var t = {
              step: a === N.g.Cb ? 1 : d(N.g.nf),
              option: d(N.g.he)
          };
          q = {
              action: "checkout",
              Qb: tx(e),
              Qa: J(c(), t)
          }
      } else
          "set_checkout_option" === a && (q = {
              action: "checkout_option",
              Qa: {
                  step: d(N.g.nf),
                  option: d(N.g.he)
              }
          });
      q && (q.Rf = d(N.g.oa));
      return q
  }, Sx = {}, fx = function(a, b) {
      var c = Sx[a];
      Sx[a] = J(b);
      if (!c)
          return !1;
      for (var d in b)
          if (b.hasOwnProperty(d) && b[d] !== c[d])
              return !0;
      for (var e in c)
          if (c.hasOwnProperty(e) && c[e] !== b[e])
              return !0;
      return !1
  };
  var Tx = hw;
  var Ux = function(a, b, c) {
      for (var d = 0; d < b.length; d++)
          a.hasOwnProperty(b[d]) && (a[b[d]] = c(a[b[d]]))
  };
  Object.freeze({
      dl: 1,
      id: 1
  });
  Object.freeze(["config", "event", "get", "set"]);
  var Vx = encodeURI
    , X = encodeURIComponent
    , Wx = function(a, b, c) {
      Ob(a, b, c)
  }
    , Xx = function(a, b) {
      if (!a)
          return !1;
      var c = xf(zf(a), "host");
      if (!c)
          return !1;
      for (var d = 0; b && d < b.length; d++) {
          var e = b[d] && b[d].toLowerCase();
          if (e) {
              var f = c.length - e.length;
              0 < f && "." != e.charAt(0) && (f--,
              e = "." + e);
              if (0 <= f && c.indexOf(e, f) == f)
                  return !0
          }
      }
      return !1
  }
    , Yx = function(a, b, c) {
      for (var d = {}, e = !1, f = 0; a && f < a.length; f++)
          a[f] && a[f].hasOwnProperty(b) && a[f].hasOwnProperty(c) && (d[a[f][b]] = a[f][c],
          e = !0);
      return e ? d : null
  };
  var Z = {
      o: {}
  };
  Z.o.e = ["google"],
  function() {
      (function(a) {
          Z.__e = a;
          Z.__e.s = "e";
          Z.__e.isVendorTemplate = !0;
          Z.__e.priorityOverride = 0;
          Z.__e.isInfrastructure = !1
      }
      )(function(a) {
          return String(a.vtp_gtmCachedValues.event)
      })
  }();
  Z.o.f = ["google"],
  function() {
      (function(a) {
          Z.__f = a;
          Z.__f.s = "f";
          Z.__f.isVendorTemplate = !0;
          Z.__f.priorityOverride = 0;
          Z.__f.isInfrastructure = !1
      }
      )(function(a) {
          var b = Ot("gtm.referrer", 1) || C.referrer;
          return b ? a.vtp_component && "URL" != a.vtp_component ? xf(zf(String(b)), a.vtp_component, a.vtp_stripWww, a.vtp_defaultPages, a.vtp_queryKey) : Nt(String(b)) : String(b)
      })
  }();
  Z.o.k = ["google"],
  function() {
      (function(a) {
          Z.__k = a;
          Z.__k.s = "k";
          Z.__k.isVendorTemplate = !0;
          Z.__k.priorityOverride = 0;
          Z.__k.isInfrastructure = !1
      }
      )(function(a) {
          return Rt(a.vtp_name, Ot("gtm.cookie", 1), !!a.vtp_decodeCookie)[0]
      })
  }();
  Z.o.u = ["google"],
  function() {
      var a = function(b) {
          return {
              toString: function() {
                  return b
              }
          }
      };
      (function(b) {
          Z.__u = b;
          Z.__u.s = "u";
          Z.__u.isVendorTemplate = !0;
          Z.__u.priorityOverride = 0;
          Z.__u.isInfrastructure = !1
      }
      )(function(b) {
          var c;
          c = (c = b.vtp_customUrlSource ? b.vtp_customUrlSource : Ot("gtm.url", 1)) || Lt();
          var d = b[a("vtp_component")];
          if (!d || "URL" == d)
              return Nt(String(c));
          var e = zf(String(c)), f;
          if ("QUERY" === d)
              a: {
                  var g = b[a("vtp_multiQueryKeys").toString()], l = b[a("vtp_queryKey").toString()] || "", m = b[a("vtp_ignoreEmptyQueryParam").toString()], n;
                  g ? ua(l) ? n = l : n = String(l).replace(/\s+/g, "").split(",") : n = [String(l)];
                  for (var p = 0; p < n.length; p++) {
                      var q = xf(e, "QUERY", void 0, void 0, n[p]);
                      if (void 0 != q && (!m || "" !== q)) {
                          f = q;
                          break a
                      }
                  }
                  f = void 0
              }
          else
              f = xf(e, d, "HOST" == d ? b[a("vtp_stripWww")] : void 0, "PATH" == d ? b[a("vtp_defaultPages")] : void 0);
          return f
      })
  }();
  Z.o.v = ["google"],
  function() {
      (function(a) {
          Z.__v = a;
          Z.__v.s = "v";
          Z.__v.isVendorTemplate = !0;
          Z.__v.priorityOverride = 0;
          Z.__v.isInfrastructure = !1
      }
      )(function(a) {
          var b = a.vtp_name;
          if (!b || !b.replace)
              return !1;
          var c = Ot(b.replace(/\\\./g, "."), a.vtp_dataLayerVersion || 1)
            , d = void 0 !== c ? c : a.vtp_defaultValue;
          Wt(d, "v", a.vtp_gtmEventId);
          return d
      })
  }();

  Z.o.smm = ["google"],
  function() {
      (function(a) {
          Z.__smm = a;
          Z.__smm.s = "smm";
          Z.__smm.isVendorTemplate = !0;
          Z.__smm.priorityOverride = 0;
          Z.__smm.isInfrastructure = !1
      }
      )(function(a) {
          var b = a.vtp_input
            , c = Yx(a.vtp_map, "key", "value") || {}
            , d = c.hasOwnProperty(b) ? c[b] : a.vtp_defaultValue;
          Wt(d, "smm", a.vtp_gtmEventId);
          return d
      })
  }();

  Z.o.gaawc = ["google"],
  function() {
      (function(a) {
          Z.__gaawc = a;
          Z.__gaawc.s = "gaawc";
          Z.__gaawc.isVendorTemplate = !0;
          Z.__gaawc.priorityOverride = 10;
          Z.__gaawc.isInfrastructure = !1
      }
      )(function(a) {
          var b = String(a.vtp_measurementId);
          if (!h(b) || 0 >= b.indexOf("-"))
              F(a.vtp_gtmOnFailure);
          else {
              var c = Yx(a.vtp_fieldsToSet, "name", "value") || {};
              if (c.hasOwnProperty(N.g.Na) || a.vtp_userProperties) {
                  var d = c[N.g.Na] || {};
                  J(Yx(a.vtp_userProperties, "name", "value"), d);
                  c[N.g.Na] = d
              }
              a.vtp_enableSendToServerContainer && a.vtp_serverContainerUrl && (c[N.g.sc] = a.vtp_serverContainerUrl,
              c[N.g.ne] = !0);
              var e = a.vtp_userDataVariable;
              e && (c[N.g.ma] = e);
              Ux(c, fe, function(f) {
                  return Da(f)
              });
              Ux(c, he, function(f) {
                  return Number(f)
              });
              c.send_page_view = a.vtp_sendPageView;
              br(Yq(b, c), a.vtp_gtmEventId, {
                  noTargetGroup: !0,
                  originatingEntity: Jp(a.vtp_gtmEntityIndex, a.vtp_gtmEntityName)
              });
              F(a.vtp_gtmOnSuccess)
          }
      })
  }();
  Z.o.gaawe = ["google"],
  function() {
      function a(f, g, l) {
          for (var m = 0; m < g.length; m++)
              f.hasOwnProperty(g[m]) && (f[g[m]] = l(f[g[m]]))
      }
      function b(f, g, l) {
          var m = {}, n = function(u, v) {
              m[u] = m[u] || v
          }, p = function(u, v, w) {
              w = void 0 === w ? !1 : w;
              c.push(6);
              if (u) {
                  m.items = m.items || [];
                  for (var x = {}, y = 0; y < u.length; x = {
                      Ub: x.Ub
                  },
                  y++)
                      x.Ub = {},
                      k(u[y], function(B) {
                          return function(D, I) {
                              w && "id" === D ? B.Ub.promotion_id = I : w && "name" === D ? B.Ub.promotion_name = I : B.Ub[D] = I
                          }
                      }(x)),
                      m.items.push(x.Ub)
              }
              if (v)
                  for (var A in v)
                      d.hasOwnProperty(A) ? n(d[A], v[A]) : n(A, v[A])
          }, q;
          "dataLayer" === f.vtp_getEcommerceDataFrom ? (q = f.vtp_gtmCachedValues.eventModel) || (q = f.vtp_gtmCachedValues.ecommerce) : (q = f.vtp_ecommerceMacroData,
          G(q) && q.ecommerce && !q.items && (q = q.ecommerce));
          if (G(q)) {
              var r = !1, t;
              for (t in q)
                  q.hasOwnProperty(t) && (r || (c.push(5),
                  r = !0),
                  "currencyCode" === t ? n("currency", q.currencyCode) : "impressions" === t && g === N.g.Va ? p(q.impressions, null) : "promoClick" === t && g === N.g.pb ? p(q.promoClick.promotions, q.promoClick.actionField, !0) : "promoView" === t && g === N.g.Wa ? p(q.promoView.promotions, q.promoView.actionField, !0) : e.hasOwnProperty(t) ? g === e[t] && p(q[t].products, q[t].actionField) : m[t] = q[t]);
              J(m, l)
          }
      }
      var c = []
        , d = {
          id: "transaction_id",
          revenue: "value",
          list: "item_list_name"
      }
        , e = {
          click: "select_item",
          detail: "view_item",
          add: "add_to_cart",
          remove: "remove_from_cart",
          checkout: "begin_checkout",
          checkout_option: "checkout_option",
          purchase: "purchase",
          refund: "refund"
      };
      (function(f) {
          Z.__gaawe = f;
          Z.__gaawe.s = "gaawe";
          Z.__gaawe.isVendorTemplate = !0;
          Z.__gaawe.priorityOverride = 0;
          Z.__gaawe.isInfrastructure = !1
      }
      )(function(f) {
          var g;
          g = f.vtp_migratedToV2 ? String(f.vtp_measurementIdOverride) : String(f.vtp_measurementIdOverride || f.vtp_measurementId);
          if (h(g) && 0 === g.indexOf("G-")) {
              var l = String(f.vtp_eventName)
                , m = {};
              c = [];
              f.vtp_sendEcommerceData && (ee.hasOwnProperty(l) || "checkout_option" === l) && b(f, l, m);
              var n = f.vtp_eventSettingsVariable;
              if (n)
                  for (var p in n)
                      n.hasOwnProperty(p) && (m[p] = n[p]);
              if (f.vtp_eventSettingsTable) {
                  var q = Yx(f.vtp_eventSettingsTable, "parameter", "parameterValue"), r;
                  for (r in q)
                      m[r] = q[r]
              }
              var t = Yx(f.vtp_eventParameters, "name", "value"), u;
              for (u in t)
                  t.hasOwnProperty(u) && (m[u] = t[u]);
              var v = f.vtp_userDataVariable;
              v && (m[N.g.ma] = v);
              if (m.hasOwnProperty(N.g.Na) || f.vtp_userProperties) {
                  var w = m[N.g.Na] || {};
                  J(Yx(f.vtp_userProperties, "name", "value"), w);
                  m[N.g.Na] = w
              }
              var x = {
                  originatingEntity: Jp(f.vtp_gtmEntityIndex, f.vtp_gtmEntityName)
              };
              if (0 < c.length) {
                  var y = {};
                  x.eventMetadata = (y.event_usage = c,
                  y)
              }
              a(m, fe, function(B) {
                  return Da(B)
              });
              a(m, he, function(B) {
                  return Number(B)
              });
              var A = f.vtp_gtmEventId;
              x.noGtmEvent = !0;
              br(Zq(g, l, m), A, x);
              F(f.vtp_gtmOnSuccess)
          } else
              F(f.vtp_gtmOnFailure)
      })
  }();

  Z.o.ua = ["google"],
  function() {
      function a(m, n) {
          for (var p in m)
              if (!l[p] && m.hasOwnProperty(p)) {
                  var q = g[p] ? Da(m[p]) : m[p];
                  "anonymizeIp" != p || q || (q = void 0);
                  n[p] = q
              }
      }
      function b(m) {
          var n = {};
          m.vtp_gaSettings && J(Yx(m.vtp_gaSettings.vtp_fieldsToSet, "fieldName", "value"), n);
          J(Yx(m.vtp_fieldsToSet, "fieldName", "value"), n);
          Da(n.urlPassthrough) && (n._useUp = !0);
          m.vtp_transportUrl && (n._x_19 = m.vtp_transportUrl);
          return n
      }
      function c(m, n) {
          return void 0 === n ? n : m(n)
      }
      function d(m, n, p) {}
      function e(m, n) {
          if (!f) {
              var p = m.vtp_useDebugVersion ? "u/analytics_debug.js" : "analytics.js";
              m.vtp_useInternalVersion && !m.vtp_useDebugVersion && (p = "internal/" + p);
              f = !0;
              var q = m.vtp_gtmOnFailure
                , r = xe || ze ? ip(n._x_19, "/analytics.js") : void 0
                , t = Ul("https:", "http:", "//www.google-analytics.com/" + p, n && !!n.forceSSL);
              U("analytics.js" === p && r ? r : t, function() {
                  var u = Vp();
                  u && u.loaded || q();
              }, q)
          }
      }
      var f, g = {
          allowAnchor: !0,
          allowLinker: !0,
          alwaysSendReferrer: !0,
          anonymizeIp: !0,
          cookieUpdate: !0,
          exFatal: !0,
          forceSSL: !0,
          javaEnabled: !0,
          legacyHistoryImport: !0,
          nonInteraction: !0,
          useAmpClientId: !0,
          useBeacon: !0,
          storeGac: !0,
          allowAdFeatures: !0,
          allowAdPersonalizationSignals: !0,
          _cd2l: !0
      }, l = {
          urlPassthrough: !0
      };
      (function(m) {
          Z.__ua = m;
          Z.__ua.s = "ua";
          Z.__ua.isVendorTemplate = !0;
          Z.__ua.priorityOverride = 0;
          Z.__ua.isInfrastructure = !1
      }
      )(function(m) {
          function n() {
              if (m.vtp_doubleClick || "DISPLAY_FEATURES" == m.vtp_advertisingFeaturesType)
                  v.displayfeatures = !0
          }
          var p = {}
            , q = {}
            , r = {};
          if (m.vtp_gaSettings) {
              var t = m.vtp_gaSettings;
              J(Yx(t.vtp_contentGroup, "index", "group"), p);
              J(Yx(t.vtp_dimension, "index", "dimension"), q);
              J(Yx(t.vtp_metric, "index", "metric"), r);
              var u = J(t);
              u.vtp_fieldsToSet = void 0;
              u.vtp_contentGroup = void 0;
              u.vtp_dimension = void 0;
              u.vtp_metric = void 0;
              m = J(m, u)
          }
          J(Yx(m.vtp_contentGroup, "index", "group"), p);
          J(Yx(m.vtp_dimension, "index", "dimension"), q);
          J(Yx(m.vtp_metric, "index", "metric"), r);
          var v = b(m)
            , w = String(m.vtp_trackingId || "")
            , x = ""
            , y = ""
            , A = "";
          m.vtp_setTrackerName && "string" == typeof m.vtp_trackerName ? "" !== m.vtp_trackerName && (A = m.vtp_trackerName,
          y = A + ".") : (A = "gtm" + Je(),
          y = A + ".");
          var B = function(ca, aa) {
              for (var xa in aa)
                  aa.hasOwnProperty(xa) && (v[ca + xa] = aa[xa])
          };
          B("contentGroup", p);
          B("dimension", q);
          B("metric", r);
          m.vtp_enableEcommerce && (x = m.vtp_gtmCachedValues.event,
          v.gtmEcommerceData = d(m, v, x));
          if ("TRACK_EVENT" === m.vtp_trackType)
              x = "track_event",
              n(),
              v.eventCategory = String(m.vtp_eventCategory),
              v.eventAction = String(m.vtp_eventAction),
              v.eventLabel = c(String, m.vtp_eventLabel),
              v.value = c(Ba, m.vtp_eventValue);
          else if ("TRACK_PAGEVIEW" == m.vtp_trackType) {
              if (x = N.g.fc,
              n(),
              "DISPLAY_FEATURES_WITH_REMARKETING_LISTS" == m.vtp_advertisingFeaturesType && (v.remarketingLists = !0),
              m.vtp_autoLinkDomains) {
                  var D = {};
                  D[N.g.N] = m.vtp_autoLinkDomains;
                  D.use_anchor = m.vtp_useHashAutoLink;
                  D[N.g.wb] = m.vtp_decorateFormsAutoLink;
                  v[N.g.wa] = D
              }
          } else
              "TRACK_SOCIAL" === m.vtp_trackType ? (x = "track_social",
              v.socialNetwork = String(m.vtp_socialNetwork),
              v.socialAction = String(m.vtp_socialAction),
              v.socialTarget = String(m.vtp_socialActionTarget)) : "TRACK_TIMING" == m.vtp_trackType && (x = "timing_complete",
              v.eventCategory = String(m.vtp_timingCategory),
              v.timingVar = String(m.vtp_timingVar),
              v.value = Ba(m.vtp_timingValue),
              v.eventLabel = c(String, m.vtp_timingLabel));
          m.vtp_enableRecaptcha && (v.enableRecaptcha = !0);
          m.vtp_enableLinkId && (v.enableLinkId = !0);
          var I = {};
          a(v, I);
          v.name || (I.gtmTrackerName = A);
          I.gaFunctionName = m.vtp_functionName;
          void 0 !== m.vtp_nonInteraction && (I.nonInteraction = m.vtp_nonInteraction);
          var H = Rm(Qm(Pm(Om(Hm(new Gm(m.vtp_gtmEventId,m.vtp_gtmPriorityId), I), m.vtp_gtmOnSuccess), m.vtp_gtmOnFailure), !0));
          rx(w, x, Date.now(), H);
          var E = Xp(m.vtp_functionName);
          if (sa(E)) {
              var L = function(ca) {
                  var aa = [].slice.call(arguments, 0);
                  aa[0] = y + aa[0];
                  E.apply(window, aa)
              };
              if ("TRACK_TRANSACTION" == m.vtp_trackType) {} else if ("DECORATE_LINK" == m.vtp_trackType) {} else if ("DECORATE_FORM" == m.vtp_trackType) {} else if ("TRACK_DATA" == m.vtp_trackType) {}
              e(m, v)
          } else
              F(m.vtp_gtmOnFailure)
      })
  }();

  Z.o.html = ["customScripts"],
  function() {
      function a(d, e, f, g) {
          return function() {
              try {
                  if (0 < e.length) {
                      var l = e.shift()
                        , m = a(d, e, f, g);
                      if ("SCRIPT" == String(l.nodeName).toUpperCase() && "text/gtmscript" == l.type) {
                          var n = C.createElement("script");
                          n.async = !1;
                          n.type = "text/javascript";
                          n.id = l.id;
                          n.text = l.text || l.textContent || l.innerHTML || "";
                          l.charset && (n.charset = l.charset);
                          var p = l.getAttribute("data-gtmsrc");
                          p && (n.src = p,
                          Hb(n, m));
                          d.insertBefore(n, null);
                          p || m()
                      } else if (l.innerHTML && 0 <= l.innerHTML.toLowerCase().indexOf("<script")) {
                          for (var q = []; l.firstChild; )
                              q.push(l.removeChild(l.firstChild));
                          d.insertBefore(l, null);
                          a(l, q, m, g)()
                      } else
                          d.insertBefore(l, null),
                          m()
                  } else
                      f()
              } catch (r) {
                  F(g)
              }
          }
      }
      function b(d) {
          if (C.body) {
              var e = d.vtp_gtmOnFailure
                , f = Xt(d.vtp_html, d.vtp_gtmOnSuccess, e)
                , g = f.Ck
                , l = f.K;
              if (d.vtp_useIframe) {} else
                  d.vtp_supportDocumentWrite ? c(g, l, e) : a(C.body, Tb(g), l, e)()
          } else
              Jt(function() {
                  b(d)
              }, 200)
      }
      Z.__html = b;
      Z.__html.s = "html";
      Z.__html.isVendorTemplate = !0;
      Z.__html.priorityOverride = 0;
      Z.__html.isInfrastructure = !1
  }();

  var rz = {};
  rz.macro = function(a) {
      if (Mc.Jf.hasOwnProperty(a))
          return Mc.Jf[a]
  }
  ,
  rz.onHtmlSuccess = Mc.Zh(!0),
  rz.onHtmlFailure = Mc.Zh(!1);
  rz.dataLayer = Qe;
  rz.callback = function(a) {
      Ge.hasOwnProperty(a) && sa(Ge[a]) && Ge[a]();
      delete Ge[a]
  }
  ;
  rz.bootstrap = 0;
  rz._spx = !1;
  function sz() {
      oe[T.C] = oe[T.C] || rz;
      T.Ua && (oe["ctid_" + T.Ua] = rz);
      li();
      oi() || k(pi(), function(a, b) {
          op(a, b.transportUrl, b.context);
          K(92)
      });
      Ka(He, Z.o);
      Nc();
      Oc = Xc
  }
  (function(a) {
      function b() {
          m = C.documentElement.getAttribute("data-tag-assistant-present");
          Ls(m) && (l = g.Dj)
      }
      if (!z["__TAGGY_INSTALLED"]) {
          var c = !1;
          if (C.referrer) {
              var d = zf(C.referrer);
              c = "cct.google" === wf(d, "host")
          }
          if (!c) {
              var e = Kh("googTaggyReferrer");
              c = e.length && e[0].length
          }
          c && (z["__TAGGY_INSTALLED"] = !0,
          Lb("https://cct.google/taggy/agent.js"))
      }
      if (Be)
          a();
      else {
          var f = function(u) {
              var v = "GTM"
                , w = "GTM";
              ve ? (v = "OGT",
              w = "GTAG") : Be && (w = v = "OPT");
              var x = z["google.tagmanager.debugui2.queue"];
              x || (x = [],
              z["google.tagmanager.debugui2.queue"] = x,
              Lb("https://" + ne.Xd + "/debug/bootstrap?id=" + T.C + "&src=" + w + "&cond=" + u + "&gtm=" + ri()));
              var y = {
                  messageType: "CONTAINER_STARTING",
                  data: {
                      scriptSource: Fb,
                      containerProduct: v,
                      debug: !1,
                      id: T.C,
                      destinations: ii()
                  }
              };
              y.data.resume = function() {
                  a()
              }
              ;
              ne.Ji && (y.data.initialPublish = !0);
              x.push(y)
          }
            , g = {
              Ql: 1,
              Ej: 2,
              Qj: 3,
              Li: 4,
              Dj: 5
          }
            , l = void 0
            , m = void 0
            , n = xf(z.location, "query", !1, void 0, "gtm_debug");
          Ls(n) && (l = g.Ej);
          if (!l && C.referrer) {
              var p = zf(C.referrer);
              "tagassistant.google.com" === wf(p, "host") && (l = g.Qj)
          }
          if (!l) {
              var q = Kh("__TAG_ASSISTANT");
              q.length && q[0].length && (l = g.Li)
          }
          l || b();
          if (!l && Ms(m)) {
              var r = function() {
                  if (t)
                      return !0;
                  t = !0;
                  b();
                  l && Fb ? f(l) : a()
              }
                , t = !1;
              Pb(C, "TADebugSignal", function() {
                  r()
              }, !1);
              z.setTimeout(function() {
                  r()
              }, 200)
          } else
              l && Fb ? f(l) : a()
      }
  }
  )(function() {
      if (R(70)) {
          var a = ho(bo.F.ef, T.C);
          io(a)
      }
      Ag().m();
      bj();
      if (T.Ua ? oe["ctid_" + T.Ua] : oe[T.C]) {
          var b = oe.zones;
          b && b.unregisterChild(hi());
      } else {
          (R(11) || R(13) || R(55) || R(48)) && Yj();
          for (var c = data.resource || {}, d = c.macros || [], e = 0; e < d.length; e++)
              Ec.push(d[e]);
          for (var f = c.tags || [], g = 0; g < f.length; g++)
              Hc.push(f[g]);
          for (var l = c.predicates || [], m = 0; m < l.length; m++)
              Gc.push(l[m]);
          for (var n = c.rules || [], p = 0; p < n.length; p++) {
              for (var q = n[p], r = {}, t = 0; t < q.length; t++)
                  r[q[t][0]] = Array.prototype.slice.call(q[t], 1);
              Fc.push(r)
          }
          Jc = Z;
          Kc = uu;
          sz();
          if (R(102)) {
              for (var u = We["7"], v = u ? u.split("|") : [], w = {}, x = 0; x < v.length; x++)
                  w[v[x]] = !0;
              for (var y = 0; y < lh.length; y++) {
                  var A = lh[y]
                    , B = w[A] ? "granted" : "denied";
                  Hg().implicit(A, B)
              }
          }
          Ks();
          Dp = !1;
          Ep = 0;
          if ("interactive" == C.readyState && !C.createEventObject || "complete" == C.readyState)
              Gp();
          else {
              Pb(C, "DOMContentLoaded", Gp);
              Pb(C, "readystatechange", Gp);
              if (C.createEventObject && C.documentElement.doScroll) {
                  var D = !0;
                  try {
                      D = !z.frameElement
                  } catch (Y) {}
                  D && Hp()
              }
              Pb(z, "load", Gp)
          }
          $r = !1;
          "complete" === C.readyState ? bs() : Pb(z, "load", bs);
          mj && z.setInterval(qj, 864E5);
          R(119) && ij.push(Mq);
          ij.push(wu);
          ij.push(Qq);
          ij.push(Nj);
          $a("HEALTH", 1);
          Fe = Ha();
          rz.bootstrap = Fe;
          if (R(70)) {
              var L = ho(bo.F.Dg, T.C);
              if (io(L)) {
                  var M = ho(bo.F.ef, T.C);
                  jo(L, M)
              }
          }
      }
  });

}
)()
