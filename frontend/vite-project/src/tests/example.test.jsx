import {describe, it, expect} from "vitest";

//This is for test cases
describe("Example Suite", ()=>{

    it("should pass",()=>{
        const sum = 2 + 2;
        expect(sum).toEqual(4);
    })

})