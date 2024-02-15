function solution(X, Y) {    
    let ans = [];
    let stack = [];
    
    for(let i = 0; i < X.length; i++){
        if(stack.includes(X[i])){
            continue;
        }
        
        const yArr = Y.split(X[i]);
        
        if(yArr.length !== 1){
            const xArr = X.split(X[i]);
            
            const min = Math.min(xArr.length - 1, yArr.length - 1);
            
            ans.push(X[i].repeat(min));
        }
        
        stack.push(X[i]);
    }
    
    if(ans.length === 0){
        return "-1";
    }
    
    if(Number(ans.join("")) === 0){
        return "0";
    }
    
    ans = ans.join("").split("").sort((a,b) => b - a);
    
    return ans.join("");
}