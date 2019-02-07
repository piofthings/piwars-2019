# Commands for communication between J2 Cruncher and J2 Controller

## Menus

<table class="table">
    <thead>
        <tr>
            <th colspan="2">
            <strong>Configure Servo Indexes</strong>
            </th>
        <tr>
    </thead>
    <tbody>
        <tr>
         <td>
            { <br>
                "cmd": "calibrate", <br>
                "action": "servoIndex", <br>
                "data": "init" <br>
            }
         </td>
         <td>
            { <br>
                "res": "OK" <br>
                "data": null <br>
            }
         </td>
        </tr>
        <tr>
            <td colspan=2>
              <table class="table">
                <thead>
                    <tr>
                        <th>Cruncher</th>
                        <th>Controller</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                         <td>
                            { <br>
                                "cmd": "calibrate" <br>
                                "action": "setupFrontLeft", <br>
                                "data": [0 - 15] <br>
                            }
                         </td>
                         <td>
                             { <br>
                                 "res": "OK", <br>
                             }
                         </td>
                     </tr>
                     <tr>
                        <td>
                           { <br>
                               "cmd": "calibrate" <br>
                               "action": "setupFrontRight", <br>
                               "data": [0 - 15] <br>
                           }
                        </td>
                        <td>
                            { <br>
                                "res": "OK", <br>
                            }
                        </td>
                        </tr>
                        <tr>
                            <td>
                               { <br>
                                   "cmd": "calibrate" <br>
                                   "action": "setupRearLeft", <br>
                                   "data": [0 - 15] <br>
                               }
                            </td>
                            <td>
                                { <br>
                                    "res": "OK", <br>
                                }
                            </td>
                        </tr>
                        <tr>
                            <td>
                               { <br>
                                   "cmd": "calibrate" <br>
                                   "action": "setupRearRight", <br>
                                   "data": [0 - 15] <br>
                               }
                            </td>
                            <td>
                                { <br>
                                    "res": "OK", <br>
                                }
                            </td>
                        </tr>
                        <tr>
                            <td>
                               { <br>
                                   "cmd": "calibrate" <br>
                                   "action": "setupSuspensionFront", <br>
                                   "data": [0 - 15] <br>
                               }
                            </td>
                            <td>
                                { <br>
                                    "res": "OK", <br>
                                }
                            </td>
                        </tr>
                        <tr>
                            <td>
                               { <br>
                                   "cmd": "calibrate" <br>
                                   "action": "setupSuspnesionRear", <br>
                                   "data": [0 - 15] <br>
                               }
                            </td>
                            <td>
                                { <br>
                                    "res": "OK", <br>
                                }
                            </td>
                        </tr>
                    </tbody>
              </table>
            </td>
        </tr>
    </tbody>
</table>

<table class="table">
  <thead>
    <tr>
      <td colspan="2">
        <strong>Calibrate Servo Zero positions</strong>
      </td>
    </tr>
  </thead>
  <tbody>
    <tr>
       <td>
          { <br>
              "cmd": "calibrate", <br>
              "action": "servoIndex", <br>
              "data": "init" <br>
          }
       </td>
       <td>
          { <br>
              "res": "OK" <br>
              "data": null <br>
          }
       </td>
    </tr>
    <tr>
      <td colspan=2>
        <table class="table">
          <thead>
            <tr>
              <th>Cruncher</th>
              <th>Controller</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                      { <br>
                          "cmd": "calibrate" <br>
                          "action": "frontLeftZero", <br>
                          "data": [0 - 160] <br>
                      }
              </td>
              <td>
                       { <br>
                           "res": "OK", <br>
                           "data": [currentPosition] <br>
                       }
              </td>
            </tr>
            <tr>
              <td>
                 { <br>
                     "cmd": "calibrate" <br>
                     "action": "frontRightZero", <br>
                     "data": [0 - 160] <br>
                 }
              </td>
              <td>
                  { <br>
                      "res": "OK", <br>
                      "data": [currentPosition] <br>
                  }
              </td>
            </tr>
            <tr>
              <td>
                 { <br>
                     "cmd": "calibrate" <br>
                     "action": "rearLeftZero", <br>
                     "data": [0 - 160] <br>
                 }
              </td>
              <td>
                  { <br>
                      "res": "OK", <br>
                      "data": [currentPosition] <br>
                  }
              </td>
            </tr>
            <tr>
                <td>
                   { <br>
                       "cmd": "calibrate" <br>
                       "action": "rearRightZero", <br>
                       "data": [0 - 160] <br>
                   }
                </td>
                <td>
                    { <br>
                        "res": "OK", <br>
                        "data": [currentPosition] <br>
                    }
                </td>
            </tr>
            <tr>
                <td>
                   { <br>
                       "cmd": "calibrate" <br>
                       "action": "suspensionFrontZero", <br>
                       "data": [0 - 160] <br>
                   }
                </td>
                <td>
                    { <br>
                        "res": "OK", <br>
                        "data": [currentPosition] <br>
                    }
                </td>
            </tr>
            <tr>
                <td>
                   { <br>
                       "cmd": "calibrate" <br>
                       "action": "suspensionRearZero", <br>
                       "data": [0 - 160] <br>
                   }
                </td>
                <td>
                    { <br>
                        "res": "OK", <br>
                        "data": [currentPosition] <br>
                    }
                </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

<table class="table">
  <thead>
    <tr>
      <th colspan="2">
      Current status
      </th>
    </tr>
    <tr>
      <th>
        Cruncher
      </th>
      <th>
        Controller
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
      {<br>
        "cmd": "calibrate", <br>
        "action": "saveStatus"<br>
        "data": null<br>
      }<br>
      </td>
      <td>
      {<br>
        "res" : "OK",<br>
        "data": [CurrentStatusJSON string]<br>
      }<br>
      </td>
    </tr>
    <tr>
      <td>
      {<br>
        "cmd": "calibrate", <br>
        "action": "getStatus"<br>
        "data": null<br>
      }<br>
      </td>
      <td>
      {<br>
        "res" : "OK",<br>
        "data": [CurrentStatusJSON string]<br>
      }<br>
      </td>
    </tr>
  </tbody>
</table>

<table class="table">
  <thead>
    <tr>
      <th colspan="2">
        Set actuation angle
      </th>
    </tr>
    <tr>
      <th>
        Cruncher
      </th>
      <th>
        Controller
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
      {<br>
        "cmd": "calibrate",<br>
        "action": "setSteeringActuationAngle",<br>
        "data": [0 - 160]<br>
        }<br>
      </td>
      <td>
      {<br>
        "res" : "OK",<br>
        "data": [CurrentStatusJSON string]<br>
      }<br>
      </td>
    </tr>
    <tr>
      <td>
      {<br>
        "cmd": "calibrate",<br>
        "action": "setSuspensionActuationAngle",<br>
        "data": [0 - 160]<br>
        }<br>
        </td>
      <td>
      {<br>
        "res" : "OK",<br>
        "data": [CurrentStatusJSON string]<br>
      }<br>
      </td>
    </tr>
  </tbody>
</table>

<table class="table">
  <thead>
    <tr>
      <th colspan=2>
        Reload status
      </th>
    </tr>
    <tr>
      <th>
      Cruncher
      </th>
      <th>
      Controller
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
      {<br>
      "cmd": "calibrate",<br>
      "action": "reloadStatus",<br>
      "data": None<br>
      }<br>
      </td>
      <td>
      {<br>
      "res" : "OK",<br>
      "data": [CurrentStatusJSON string]<br>
      }<br>
      </td>
    </tr>
  </tbody>
</table>

## Manual Control

<table class="table">
 <thead>
  <tr>
   <th colspan="2">Pi Noon Commands</th>
  </tr>
  <tr>
   <th>Cruncher</th>
   <th>Controller</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
   ```json
    {  
     "cmd": "steering",
     "action": "move",
     "data": {
         "speedLeft": [0-1],
         "directionLeft": [1-0],
         "speedRight": [0-1],
         "directionRight": [1-0]
     }
    }
    ```
   </td>
   <td></td>
  </tr>
 </tbody>
</table>
