
my_map :: (a -> b) -> [a] -> [b]
my_map f l =
  if length l ==  0 then []
  else [f (head l)] ++ my_map f (tail l)


my_filter :: (a -> Bool) -> [a] -> [a]
my_filter p l =
  if length l == 0 then []
  else (if p (head l) then [head l] else []) ++ my_filter p (tail l)


my_foldl :: (a -> a -> a) -> a -> [a] -> a
my_foldl f u l =
  if length l == 1 then (f u (head l))
  else my_foldl f (f u (head l)) (tail l)


my_foldr :: (a -> a -> a) -> a -> [a] -> a
my_foldr f u l =
  if length l == 1 then (f (last l) u)
  else my_foldr f (f (last l) u) (init l)


my_zip :: (a -> b -> c) -> [a] -> [b] -> [c]
my_zip f l1 l2 =
  if length l1 == 0 then []
  else [f (head l1) (head  l2)] ++ my_zip f (tail l1) (tail l2)


addXY :: Int -> Int -> Int
addXY x y = x + y

squareX :: Int -> Int
squareX x = x * x

func1 :: [Int] -> Int
func1 l = my_foldl addXY 0 (my_map squareX l)

isLengthEven :: String -> Bool
isLengthEven a =
  if (length a) `mod` 2 == 0 then True
  else False

stringCombine :: String -> String -> String
stringCombine s1 s2 = (s1 ++ " " ++ s2)

initials :: String -> String
initials s = (take 1 s) ++ "."

func2 :: [f] -> [m] -> [l] -> j
func2 l1 l2 l3 =
  my_filter isLengthEven
    (my_zip stringCombine
      (my_zip stringCombine
       l1 (my_map initials l2)) l3)

