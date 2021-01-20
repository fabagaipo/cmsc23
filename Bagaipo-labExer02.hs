-----Easy Functions-----
cube :: Int -> Int
cube x = x * x * x

double :: Int -> Int
double x = x * 2

-----Recursive Functions-----
modulus :: Int -> Int -> Int
modulus x y = if (x < y) then x else modulus (x - y) y 

factorial :: Int -> Int
factorial x = if (x < 2) then 1 else x * factorial ( x - 1)

-----Higher Order Functions-----
compose :: (Int -> Int) -> (Int -> Int) -> (Int -> Int)
compose f g = (\h -> f(g h))

subtractMaker :: Int -> (Int -> Int)
subtractMaker x = (\y -> y - x)

applyNTimes :: (Int -> Int) -> Int -> Int -> Int
applyNTimes f n x = if (n == 1) then f(x) else applyNTimes f (n - 1) (f x)
