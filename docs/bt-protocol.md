# Commands for communication between J2 Cruncher and J2 Controller

## Calibration Menu
<table class="table">
    <thead>
        <tr>
            <td colspan="2">
            <strong>Configure Servo Indexes</strong>
            </td>
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
                                "action": "frontLeft", <br>
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
                               "action": "frontRight", <br>
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
                                   "action": "rearLeft", <br>
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
                                   "action": "rearRight", <br>
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
