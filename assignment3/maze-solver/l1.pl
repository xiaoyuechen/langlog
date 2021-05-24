:- use_module(library(lists)).
:- use_module(library(pairs)).

walkable(Pos) :-
	black(Pos); food(Pos); treasure(Pos); start(Pos); exit(Pos).

neighbour([X1, Y1], [X2, Y2]) :- X1 =:= X2, (Y1 =:= Y2 - 1; Y1 =:= Y2 + 1).
neighbour([X1, Y1], [X2, Y2]) :- Y1 =:= Y2, (X1 =:= X2 - 1; X1 =:= X2 + 1).

move(From, To) :-
	walkable(From), walkable(To),
	neighbour(From, To).

same([X1, Y1], [X2, Y2]) :- X1 =:= X2, Y1 =:= Y2.

dfs(From, To, Path) :-
	dfs_impl(From, To, [], Path0),
	reverse(Path0, Path).
dfs_impl(From, To, Path, [From | Path]) :- same(From, To).
dfs_impl(From, To, Path, Sol) :-
	move(From, Next),
	not(member(Next, Path)),
	dfs_impl(Next, To, [From | Path], Sol).

shortest(From, To, Path) :-
	findall(Path0, dfs(From, To, Path0), Paths),
	map_list_to_pairs(length, Paths, Pairs0),
	keysort(Pairs0, Pairs),
	[_-Path | _] = Pairs.

solve(Path) :-
	start(S), exit(T),
	shortest(S, T, Path).
