import * as bunyan  from "bunyan";
import { ApiController } from "./api-controller";

export class BaseController implements ApiController {
    logger: bunyan;
    constructor(logger: any){
        this.logger = logger;
    }

    public getLogger() {
        return this.logger;
    }

    public isLoggedIn = (req: Express.Request): boolean =>{
        return false;
    }
}
