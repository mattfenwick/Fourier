var DATA = {
  "sine": {
    "name": "Sine wave",
    "description": "blah blah blah",
    "series": [
      {
        "name": "um ... sine 1",
//        "a": ..., // amplitude
//        "w": ..., // omega
//        ... other parameters ...
        "time": [ // time-domain data
          [1,2,3], // reals
          [3,2,1]  // imaginaries
        ],
        "freq": [ // frequency-domain data
          [2,3,4], 
          [4,3,2]
        ]
      }
    ]
  },
  "exponential": {
    "name": "Exponential decay",
    "series": [
      {
        "name": "umm ... exp 1",
        "time": [
          [1.1, 1.3, 1.2],
          [2.2, 2.4, 2.3]
        ], 
        "freq": [
          [3.3, 2.8, 2.91], 
          [3.1, 2.998, 2.41]
        ]
      },
      {
        "name": "umm ... exp 2", 
        "time": [
          [4,3,2,1],
          [8, 6, 7, 5]
        ], 
        "freq": [
          [1,2,3,4], 
          [3, 4, 1, 2]
        ]
      }
    ]
  },
//  "transients": {...}
//  ...
}
