  ## Binary Tree 
                        N1
                       /  \ 
                      /    \ 
                     /      \ 
                    N2      N3
                   / \      / \ 
                  /   \    /   \ 
                 /     \  N6   N7
                N4     N5        
               / \ 
              /   \ 
             N8   N9

<h4>Binary Tree Traversal:</h4>  
     <ol>
  <li>Preorder Traversal:</li>
  <h5>Root -> Left sub-tree -> Right sub-tree </h5>
        N1 -> N2 -> N4 -> N8 -> N9 -> N5 -> N3 -> N6 -> N7
  </br>
  </br>
  <li>InOrder Traversal:</li>
    <h5>Left sub-tree -> Root -> Right sub-tree</h5>
        N8 -> N4 -> N9 -> N2 -> N5 -> N1 -> N6 -> N3 -> N7
 </br>
 </br>
 <li>Postorder Traversal:</li>
  <h5>Left sub-tree -> Right sub-tree -> Root</h5>
       N8 -> N9 -> N4 -> N5 -> N2 -> N6 -> N7 -> N3 -> N1       
  </br>
  </br>
  <li>LevelOrder Traversal:</li>
  <h5>Level 0 -> Level 1 -> Level 2 and so on<h5>
      N1 -> N2 -> N3 -> N4 -> N5 -> N6 -> N7 -> N8 -> N9  
  </br>
  </br>
  <li>Inverting a Binary Tree:</li> 
  <h5>Original: N1 -> N2 -> N3 -> N4 -> N5 -> N6 -> N7 -> N8 -> N9</h5>                 
    <h5>Inverted: N1 -> N3 -> N2 -> N7 -> N6 -> N5 -> N4 -> N9 -> N8</h5>  
  </ol>
  
                                   Original:               Inverted:          
                                        N1                     N1
                                       /  \                   /  \ 
                                      /    \                 /    \               
                                     /      \               /      \ 
                                    N2      N3             N3       N2  
                                   / \      / \           / \       / \  
                                  /   \    /   \         /   \     /   \ 
                                 /     \  N6   N7       N7   N6   N5    N4     
                                N4     N5                               / \ 
                               / \                                     /   \   
                              /   \                                   N9   N8
                             N8   N9                   
                                                                                
   
    
