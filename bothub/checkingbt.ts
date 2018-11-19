import { BluetoothSerialPort, BluetoothSerialPortServer } from "bluetooth-serial-port";

export class demo {
    address : string = "B8:27:EB:3B:AF:70";
    btSerial : BluetoothSerialPort = new BluetoothSerialPort();
    constructor(){
        this.btSerial.findSerialPortChannel(this.address, (channel: number) => {
            this.btSerial.connect(this.address, channel, () => {
                let messageBuffer = Buffer.from("Yay!");
                this.btSerial.write(messageBuffer, (err) => {
                    if (err) {
                        console.error(err);
                    }
                });
            }, (err?: Error) => {
                if (err) {
                    console.error(err);
                }
            });
            this.btSerial.on("data", (buffer: Buffer) => console.log(buffer.toString("ascii")));
        }, () => {
            console.error("Cannot find channel!");
        });
    }

}

var demos = new demo();
