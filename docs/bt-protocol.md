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
            {   
                "cmd": "calibrate",   
                "action": "servoIndex",   
                "data": "init"   
            }
         </td>
         <td>
            {   
                "res": "OK"   
                "data": null   
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
                            {   
                                "cmd": "calibrate"   
                                "action": "setupFrontLeft",   
                                "data": [0 - 15]   
                            }
                         </td>
                         <td>
                             {   
                                 "res": "OK",   
                             }
                         </td>
                     </tr>
                     <tr>
                        <td>
                           {   
                               "cmd": "calibrate"   
                               "action": "setupFrontRight",   
                               "data": [0 - 15]   
                           }
                        </td>
                        <td>
                            {   
                                "res": "OK",   
                            }
                        </td>
                        </tr>
                        <tr>
                            <td>
                               {   
                                   "cmd": "calibrate"   
                                   "action": "setupRearLeft",   
                                   "data": [0 - 15]   
                               }
                            </td>
                            <td>
                                {   
                                    "res": "OK",   
                                }
                            </td>
                        </tr>
                        <tr>
                            <td>
                               {   
                                   "cmd": "calibrate"   
                                   "action": "setupRearRight",   
                                   "data": [0 - 15]   
                               }
                            </td>
                            <td>
                                {   
                                    "res": "OK",   
                                }
                            </td>
                        </tr>
                        <tr>
                            <td>
                               {   
                                   "cmd": "calibrate"   
                                   "action": "setupSuspensionFront",   
                                   "data": [0 - 15]   
                               }
                            </td>
                            <td>
                                {   
                                    "res": "OK",   
                                }
                            </td>
                        </tr>
                        <tr>
                            <td>
                               {   
                                   "cmd": "calibrate"   
                                   "action": "setupSuspnesionRear",   
                                   "data": [0 - 15]   
                               }
                            </td>
                            <td>
                                {   
                                    "res": "OK",   
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
          {   
              "cmd": "calibrate",   
              "action": "servoIndex",   
              "data": "init"   
          }
       </td>
       <td>
          {   
              "res": "OK"   
              "data": null   
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
                      {   
                          "cmd": "calibrate"   
                          "action": "frontLeftZero",   
                          "data": [0 - 160]   
                      }
              </td>
              <td>
                       {   
                           "res": "OK",   
                           "data": [currentPosition]   
                       }
              </td>
            </tr>
            <tr>
              <td>
                 {   
                     "cmd": "calibrate"   
                     "action": "frontRightZero",   
                     "data": [0 - 160]   
                 }
              </td>
              <td>
                  {   
                      "res": "OK",   
                      "data": [currentPosition]   
                  }
              </td>
            </tr>
            <tr>
              <td>
                 {   
                     "cmd": "calibrate"   
                     "action": "rearLeftZero",   
                     "data": [0 - 160]   
                 }
              </td>
              <td>
                  {   
                      "res": "OK",   
                      "data": [currentPosition]   
                  }
              </td>
            </tr>
            <tr>
                <td>
                   {   
                       "cmd": "calibrate"   
                       "action": "rearRightZero",   
                       "data": [0 - 160]   
                   }
                </td>
                <td>
                    {   
                        "res": "OK",   
                        "data": [currentPosition]   
                    }
                </td>
            </tr>
            <tr>
                <td>
                   {   
                       "cmd": "calibrate"   
                       "action": "suspensionFrontZero",   
                       "data": [0 - 160]   
                   }
                </td>
                <td>
                    {   
                        "res": "OK",   
                        "data": [currentPosition]   
                    }
                </td>
            </tr>
            <tr>
                <td>
                   {   
                       "cmd": "calibrate"   
                       "action": "suspensionRearZero",   
                       "data": [0 - 160]   
                   }
                </td>
                <td>
                    {   
                        "res": "OK",   
                        "data": [currentPosition]   
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
      {  
        "cmd": "calibrate",   
        "action": "saveStatus"  
        "data": null  
      }  
      </td>
      <td>
      {  
        "res" : "OK",  
        "data": [CurrentStatusJSON string]  
      }  
      </td>
    </tr>
    <tr>
      <td>
      {  
        "cmd": "calibrate",   
        "action": "getStatus"  
        "data": null  
      }  
      </td>
      <td>
      {  
        "res" : "OK",  
        "data": [CurrentStatusJSON string]  
      }  
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
      {  
        "cmd": "calibrate",  
        "action": "setSteeringActuationAngle",  
        "data": [0 - 160]  
        }  
      </td>
      <td>
      {  
        "res" : "OK",  
        "data": [CurrentStatusJSON string]  
      }  
      </td>
    </tr>
    <tr>
      <td>
      {  
        "cmd": "calibrate",  
        "action": "setSuspensionActuationAngle",  
        "data": [0 - 160]  
        }  
        </td>
      <td>
      {  
        "res" : "OK",  
        "data": [CurrentStatusJSON string]  
      }  
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
      {  
      "cmd": "calibrate",  
      "action": "reloadStatus",  
      "data": None  
      }  
      </td>
      <td>
      {  
      "res" : "OK",  
      "data": [CurrentStatusJSON string]  
      }  
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
   </td>
   <td>
    {  
        "res": "OK",  
        "data": None  
    }  
   </td>
  </tr>
  <tr>
   <td>
   {  
    "cmd": "wheels",  
    "action": "strafe",  
    "data":  { "speedLeft": [0-1], <br/>"directionLeft": [0 or 1], <br/>"speedRight": [0-1], <br/>"directionRight": [0 or 1]   <br/>
   }
   </td>
   <td>
   {  
       "res": "OK",  
       "data": None  
   }
   </td>
  </tr>

 </tbody>
</table>

<table class="table">
 <thead>
  <tr>
   <th colspan="2">Space Invaders - Apart from the PiNoon commands, this has additional commands for Aiming lasers and shooting cannons</th>
  </tr>
  <tr>
   <th>Cruncher</th>
   <th>Controller</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    {  
     "cmd": "cannon",  <br />
     "action": "aim",  <br />
     "data": {  <br />
         "position": [1-5] <br />
     }  
    }
   </td>
   <td>
    {  
        "res": "OK",  
        "data": None  
    }  
   </td>
  </tr>
  <tr>
   <td>
   {  
    "cmd": "cannon", <br />
    "action": "launch", <br />
    "data":  { <br />
        "position" : [1-5] <br />
    } <br />
   }
   </td>
   <td>
   {  
       "res": "OK",  
       "data": None  
   }
   </td>
  </tr>
 </tbody>
</table>
