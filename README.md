public class Solution {
    public ArrayList<ArrayList<Integer>> res = null;
    public ArrayList<ArrayList<Integer>> combine(int n, int k) {
        res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> temp = new ArrayList<Integer>();
        dfs(temp, 1, k, n);
        return res;
    }
    public void dfs(ArrayList<Integer> temp, int pose, int end, int all){
        if(pose == end){
            ArrayList<Integer> temp2 = new ArrayList<Integer>(temp);
            res.add(new ArrayList<Integer>(temp2));
            return;
        }
        else{
            for(int i = pose; i <= all; i++){
                temp.add(i);
                dfs(temp, pose + 1, end, all);
                temp.remove(temp.size() - 1);
            }
        }
    }
}
